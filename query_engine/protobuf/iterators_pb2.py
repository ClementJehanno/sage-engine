# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iterators.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='iterators.proto',
  package='iterators',
  syntax='proto3',
  serialized_pb=_b('\n\x0fiterators.proto\x12\titerators\"C\n\rTriplePattern\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x11\n\tpredicate\x18\x02 \x01(\t\x12\x0e\n\x06object\x18\x03 \x01(\t\"b\n\x11SavedScanIterator\x12(\n\x06triple\x18\x01 \x01(\x0b\x32\x18.iterators.TriplePattern\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x13\n\x0b\x63\x61rdinality\x18\x03 \x01(\x03\"\xe0\x01\n\x17SavedProjectionIterator\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x33\n\x0bscan_source\x18\x02 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x00\x12<\n\nnlj_source\x18\x03 \x01(\x0b\x32&.iterators.SavedNestedLoopJoinIteratorH\x00\x12\x38\n\x0cunion_source\x18\x04 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x00\x42\x08\n\x06source\"\xbd\x02\n\x1bSavedNestedLoopJoinIterator\x12\x33\n\x0bscan_source\x18\x01 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x00\x12<\n\nnlj_source\x18\x02 \x01(\x0b\x32&.iterators.SavedNestedLoopJoinIteratorH\x00\x12\'\n\x05inner\x18\x03 \x01(\x0b\x32\x18.iterators.TriplePattern\x12<\n\x03muc\x18\x04 \x03(\x0b\x32/.iterators.SavedNestedLoopJoinIterator.MucEntry\x12\x0e\n\x06offset\x18\x05 \x01(\x04\x1a*\n\x08MucEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x06source\"\xf9\x02\n\x15SavedBagUnionIterator\x12\x31\n\tscan_left\x18\x01 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x00\x12:\n\x08nlj_left\x18\x02 \x01(\x0b\x32&.iterators.SavedNestedLoopJoinIteratorH\x00\x12\x36\n\nunion_left\x18\x03 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x00\x12\x32\n\nscan_right\x18\x04 \x01(\x0b\x32\x1c.iterators.SavedScanIteratorH\x01\x12;\n\tnlj_right\x18\x05 \x01(\x0b\x32&.iterators.SavedNestedLoopJoinIteratorH\x01\x12\x37\n\x0bunion_right\x18\x06 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x01\x42\x06\n\x04leftB\x07\n\x05right\"\x89\x01\n\x08RootTree\x12\x39\n\x0bproj_source\x18\x01 \x01(\x0b\x32\".iterators.SavedProjectionIteratorH\x00\x12\x38\n\x0cunion_source\x18\x02 \x01(\x0b\x32 .iterators.SavedBagUnionIteratorH\x00\x42\x08\n\x06sourceb\x06proto3')
)




_TRIPLEPATTERN = _descriptor.Descriptor(
  name='TriplePattern',
  full_name='iterators.TriplePattern',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject', full_name='iterators.TriplePattern.subject', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predicate', full_name='iterators.TriplePattern.predicate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object', full_name='iterators.TriplePattern.object', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=97,
)


_SAVEDSCANITERATOR = _descriptor.Descriptor(
  name='SavedScanIterator',
  full_name='iterators.SavedScanIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='triple', full_name='iterators.SavedScanIterator.triple', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='iterators.SavedScanIterator.offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardinality', full_name='iterators.SavedScanIterator.cardinality', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=197,
)


_SAVEDPROJECTIONITERATOR = _descriptor.Descriptor(
  name='SavedProjectionIterator',
  full_name='iterators.SavedProjectionIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='iterators.SavedProjectionIterator.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_source', full_name='iterators.SavedProjectionIterator.scan_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nlj_source', full_name='iterators.SavedProjectionIterator.nlj_source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_source', full_name='iterators.SavedProjectionIterator.union_source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.SavedProjectionIterator.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=200,
  serialized_end=424,
)


_SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY = _descriptor.Descriptor(
  name='MucEntry',
  full_name='iterators.SavedNestedLoopJoinIterator.MucEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='iterators.SavedNestedLoopJoinIterator.MucEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='iterators.SavedNestedLoopJoinIterator.MucEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=692,
  serialized_end=734,
)

_SAVEDNESTEDLOOPJOINITERATOR = _descriptor.Descriptor(
  name='SavedNestedLoopJoinIterator',
  full_name='iterators.SavedNestedLoopJoinIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_source', full_name='iterators.SavedNestedLoopJoinIterator.scan_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nlj_source', full_name='iterators.SavedNestedLoopJoinIterator.nlj_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inner', full_name='iterators.SavedNestedLoopJoinIterator.inner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='muc', full_name='iterators.SavedNestedLoopJoinIterator.muc', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='iterators.SavedNestedLoopJoinIterator.offset', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.SavedNestedLoopJoinIterator.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=427,
  serialized_end=744,
)


_SAVEDBAGUNIONITERATOR = _descriptor.Descriptor(
  name='SavedBagUnionIterator',
  full_name='iterators.SavedBagUnionIterator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scan_left', full_name='iterators.SavedBagUnionIterator.scan_left', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nlj_left', full_name='iterators.SavedBagUnionIterator.nlj_left', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_left', full_name='iterators.SavedBagUnionIterator.union_left', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan_right', full_name='iterators.SavedBagUnionIterator.scan_right', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nlj_right', full_name='iterators.SavedBagUnionIterator.nlj_right', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_right', full_name='iterators.SavedBagUnionIterator.union_right', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='left', full_name='iterators.SavedBagUnionIterator.left',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='right', full_name='iterators.SavedBagUnionIterator.right',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=747,
  serialized_end=1124,
)


_ROOTTREE = _descriptor.Descriptor(
  name='RootTree',
  full_name='iterators.RootTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proj_source', full_name='iterators.RootTree.proj_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_source', full_name='iterators.RootTree.union_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source', full_name='iterators.RootTree.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1127,
  serialized_end=1264,
)

_SAVEDSCANITERATOR.fields_by_name['triple'].message_type = _TRIPLEPATTERN
_SAVEDPROJECTIONITERATOR.fields_by_name['scan_source'].message_type = _SAVEDSCANITERATOR
_SAVEDPROJECTIONITERATOR.fields_by_name['nlj_source'].message_type = _SAVEDNESTEDLOOPJOINITERATOR
_SAVEDPROJECTIONITERATOR.fields_by_name['union_source'].message_type = _SAVEDBAGUNIONITERATOR
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['scan_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['scan_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['nlj_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['nlj_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDPROJECTIONITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDPROJECTIONITERATOR.fields_by_name['union_source'])
_SAVEDPROJECTIONITERATOR.fields_by_name['union_source'].containing_oneof = _SAVEDPROJECTIONITERATOR.oneofs_by_name['source']
_SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY.containing_type = _SAVEDNESTEDLOOPJOINITERATOR
_SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['scan_source'].message_type = _SAVEDSCANITERATOR
_SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['nlj_source'].message_type = _SAVEDNESTEDLOOPJOINITERATOR
_SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['inner'].message_type = _TRIPLEPATTERN
_SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['muc'].message_type = _SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY
_SAVEDNESTEDLOOPJOINITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['scan_source'])
_SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['scan_source'].containing_oneof = _SAVEDNESTEDLOOPJOINITERATOR.oneofs_by_name['source']
_SAVEDNESTEDLOOPJOINITERATOR.oneofs_by_name['source'].fields.append(
  _SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['nlj_source'])
_SAVEDNESTEDLOOPJOINITERATOR.fields_by_name['nlj_source'].containing_oneof = _SAVEDNESTEDLOOPJOINITERATOR.oneofs_by_name['source']
_SAVEDBAGUNIONITERATOR.fields_by_name['scan_left'].message_type = _SAVEDSCANITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['nlj_left'].message_type = _SAVEDNESTEDLOOPJOINITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['union_left'].message_type = _SAVEDBAGUNIONITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['scan_right'].message_type = _SAVEDSCANITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['nlj_right'].message_type = _SAVEDNESTEDLOOPJOINITERATOR
_SAVEDBAGUNIONITERATOR.fields_by_name['union_right'].message_type = _SAVEDBAGUNIONITERATOR
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['scan_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['scan_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['nlj_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['nlj_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['left'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['union_left'])
_SAVEDBAGUNIONITERATOR.fields_by_name['union_left'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['left']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['scan_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['scan_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['nlj_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['nlj_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_SAVEDBAGUNIONITERATOR.oneofs_by_name['right'].fields.append(
  _SAVEDBAGUNIONITERATOR.fields_by_name['union_right'])
_SAVEDBAGUNIONITERATOR.fields_by_name['union_right'].containing_oneof = _SAVEDBAGUNIONITERATOR.oneofs_by_name['right']
_ROOTTREE.fields_by_name['proj_source'].message_type = _SAVEDPROJECTIONITERATOR
_ROOTTREE.fields_by_name['union_source'].message_type = _SAVEDBAGUNIONITERATOR
_ROOTTREE.oneofs_by_name['source'].fields.append(
  _ROOTTREE.fields_by_name['proj_source'])
_ROOTTREE.fields_by_name['proj_source'].containing_oneof = _ROOTTREE.oneofs_by_name['source']
_ROOTTREE.oneofs_by_name['source'].fields.append(
  _ROOTTREE.fields_by_name['union_source'])
_ROOTTREE.fields_by_name['union_source'].containing_oneof = _ROOTTREE.oneofs_by_name['source']
DESCRIPTOR.message_types_by_name['TriplePattern'] = _TRIPLEPATTERN
DESCRIPTOR.message_types_by_name['SavedScanIterator'] = _SAVEDSCANITERATOR
DESCRIPTOR.message_types_by_name['SavedProjectionIterator'] = _SAVEDPROJECTIONITERATOR
DESCRIPTOR.message_types_by_name['SavedNestedLoopJoinIterator'] = _SAVEDNESTEDLOOPJOINITERATOR
DESCRIPTOR.message_types_by_name['SavedBagUnionIterator'] = _SAVEDBAGUNIONITERATOR
DESCRIPTOR.message_types_by_name['RootTree'] = _ROOTTREE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TriplePattern = _reflection.GeneratedProtocolMessageType('TriplePattern', (_message.Message,), dict(
  DESCRIPTOR = _TRIPLEPATTERN,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.TriplePattern)
  ))
_sym_db.RegisterMessage(TriplePattern)

SavedScanIterator = _reflection.GeneratedProtocolMessageType('SavedScanIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDSCANITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedScanIterator)
  ))
_sym_db.RegisterMessage(SavedScanIterator)

SavedProjectionIterator = _reflection.GeneratedProtocolMessageType('SavedProjectionIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDPROJECTIONITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedProjectionIterator)
  ))
_sym_db.RegisterMessage(SavedProjectionIterator)

SavedNestedLoopJoinIterator = _reflection.GeneratedProtocolMessageType('SavedNestedLoopJoinIterator', (_message.Message,), dict(

  MucEntry = _reflection.GeneratedProtocolMessageType('MucEntry', (_message.Message,), dict(
    DESCRIPTOR = _SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY,
    __module__ = 'iterators_pb2'
    # @@protoc_insertion_point(class_scope:iterators.SavedNestedLoopJoinIterator.MucEntry)
    ))
  ,
  DESCRIPTOR = _SAVEDNESTEDLOOPJOINITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedNestedLoopJoinIterator)
  ))
_sym_db.RegisterMessage(SavedNestedLoopJoinIterator)
_sym_db.RegisterMessage(SavedNestedLoopJoinIterator.MucEntry)

SavedBagUnionIterator = _reflection.GeneratedProtocolMessageType('SavedBagUnionIterator', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDBAGUNIONITERATOR,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.SavedBagUnionIterator)
  ))
_sym_db.RegisterMessage(SavedBagUnionIterator)

RootTree = _reflection.GeneratedProtocolMessageType('RootTree', (_message.Message,), dict(
  DESCRIPTOR = _ROOTTREE,
  __module__ = 'iterators_pb2'
  # @@protoc_insertion_point(class_scope:iterators.RootTree)
  ))
_sym_db.RegisterMessage(RootTree)


_SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY.has_options = True
_SAVEDNESTEDLOOPJOINITERATOR_MUCENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
