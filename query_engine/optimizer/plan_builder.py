# plan_builder.py
# Author: Thomas MINIER - MIT License 2017-2018
from query_engine.iterators.projection import ProjectionIterator
from query_engine.iterators.scan import ScanIterator
from query_engine.iterators.nlj import IndexJoinIterator
from query_engine.iterators.filter import FilterIterator
from query_engine.iterators.union import BagUnionIterator
from query_engine.iterators.loader import load
from query_engine.optimizer.utils import find_connected_pattern, get_vars
from functools import reduce


def build_query_plan(query, db_connector, saved_plan=None, projection=None):
    cardinalities = []
    if saved_plan is not None:
        return load(saved_plan, db_connector), []

    # optional = query['optional'] if 'optional' in query and len(query['optional']) > 0 else None
    root = None

    if query['type'] == 'union':
        print('build union plan')
        root, cardinalities = build_union_plan(query['union'], db_connector, projection)
        print('done union plan')
    elif query['type'] == 'bgp':
        print('build join plan')
        root, cardinalities = build_join_plan(query['bgp'], db_connector, projection=projection)
        print('build join done')
    else:
        raise Exception('Unkown query type found during query optimization')

    # apply filter clause(s)
    if 'filters' in query and len(query['filters']) > 0:
        # reduce all filters in a conjunctive expression
        expression = reduce(lambda x, y: "({}) && ({})".format(x, y), query['filters'])
        root = FilterIterator(root, expression)
    return root, cardinalities


def build_union_plan(union, db_connector, projection=None):
    """Build a Bushy tree of Unions, where leaves are BGPs, from a list of BGPS"""

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def mapper(duo):
        """Build a join between two source iterators"""
        if len(duo) == 1:
            return duo[0]
        return BagUnionIterator(duo[0], duo[1])
    sources = []
    cardinalities = []
    for bgp in union:
        iterator, cards = build_join_plan(bgp, db_connector, projection=projection)
        sources.append(iterator)
        cardinalities += cards
    if len(sources) == 1:
        return sources[0], cardinalities
    while len(sources) > 1:
        sources = list(map(mapper, chunks(sources, 2)))
    return sources[0], cardinalities


def build_join_plan(bgp, db_connector, projection=None):
    """Build a join plan between a BGP and a possible OPTIONAL clause"""
    print('build left plan')
    iterator, query_vars, cardinalities = build_left_plan(bgp, db_connector)
    print('left plan done')
    # if optional is not None:
    #     iterator, query_vars, c = build_left_plan(optional, db_connector, source=iterator, base_vars=query_vars, optional=True)
    #     cardinalities += c
    values = projection if projection is not None else query_vars
    return ProjectionIterator(iterator, values), cardinalities


def build_left_plan(bgp, db_connector, source=None, base_vars=None):
    """Build a Left-linear tree of joins/left-joins from a BGP/OPTIONAL BGP"""
    # gather metadata about triple patterns
    triples = []
    cardinalities = []
    for triple in bgp:
        print('before search')
        it, c = db_connector.search(triple['subject'], triple['predicate'], triple['object'])
        triples += [{'triple': triple, 'cardinality': c, 'iterator': it}]
        cardinalities += [{'triple': triple, 'cardinality': c}]
        print('after search')
    # sort triples by ascending cardinality
    triples = sorted(triples, key=lambda v: v['cardinality'])
    # if no input iterator provided, build a Scan with the most selective pattern
    if source is None:
        pattern = triples.pop(0)
        acc = ScanIterator(pattern['iterator'], pattern['triple'], pattern['cardinality'])
        query_vars = get_vars(pattern['triple'])
    else:
        pattern = None
        acc = source
        query_vars = base_vars
    # build the left linear tree
    while len(triples) > 0:
        pattern, pos, query_vars = find_connected_pattern(query_vars, triples)
        # no connected pattern = disconnected BGP => pick the first remaining pattern in the BGP
        if pattern is None:
            pattern = triples[0]
            query_vars = query_vars | get_vars(pattern['triple'])
            pos = 0
        acc = IndexJoinIterator(acc, pattern['triple'], db_connector)
        triples.pop(pos)
    return acc, query_vars, cardinalities
