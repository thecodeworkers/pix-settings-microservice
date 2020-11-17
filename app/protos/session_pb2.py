# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='session.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rsession.proto\"\x0e\n\x0cSessionEmpty\"\x1e\n\x10SessionIdRequest\x12\n\n\x02id\x18\x01 \x02(\t\"2\n\x11SessionOneRequest\x12\x11\n\tuserAgent\x18\x01 \x02(\t\x12\n\n\x02ip\x18\x02 \x02(\t\"\x80\x01\n\x13SessionNotIdRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0b\n\x03\x61pp\x18\x02 \x02(\t\x12\n\n\x02ip\x18\x03 \x02(\t\x12\x10\n\x08location\x18\x04 \x02(\t\x12\x11\n\tuserAgent\x18\x05 \x02(\t\x12\r\n\x05valid\x18\x06 \x02(\x08\x12\x0e\n\x06\x61\x63tive\x18\x07 \x02(\x08\"\x87\x01\n\x0eSessionRequest\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x0b\n\x03\x61pp\x18\x03 \x02(\t\x12\n\n\x02ip\x18\x04 \x02(\t\x12\x10\n\x08location\x18\x05 \x02(\t\x12\x11\n\tuserAgent\x18\x06 \x02(\t\x12\r\n\x05valid\x18\x07 \x02(\x08\x12\x0e\n\x06\x61\x63tive\x18\x08 \x02(\x08\"I\n\x13SessionTableRequest\x12\x0c\n\x04page\x18\x01 \x02(\x05\x12\x14\n\x08per_page\x18\x02 \x01(\x05:\x02\x31\x35\x12\x0e\n\x06search\x18\x03 \x01(\t\"3\n\x0fSessionResponse\x12 \n\x07session\x18\x01 \x02(\x0b\x32\x0f.SessionRequest\";\n\x17SessionMultipleResponse\x12 \n\x07session\x18\x01 \x03(\x0b\x32\x0f.SessionRequest\"~\n\x14SessionTableResponse\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.SessionRequest\x12\x0c\n\x04page\x18\x02 \x02(\x05\x12\x10\n\x08per_page\x18\x03 \x02(\x05\x12\x13\n\x0btotal_items\x18\x04 \x02(\x05\x12\x11\n\tnum_pages\x18\x05 \x02(\x05\x32\xa9\x02\n\x07Session\x12\x34\n\x05table\x12\x14.SessionTableRequest\x1a\x15.SessionTableResponse\x12\x32\n\x07get_all\x12\r.SessionEmpty\x1a\x18.SessionMultipleResponse\x12+\n\x03get\x12\x12.SessionOneRequest\x1a\x10.SessionResponse\x12.\n\x04save\x12\x14.SessionNotIdRequest\x1a\x10.SessionResponse\x12+\n\x06update\x12\x0f.SessionRequest\x1a\x10.SessionResponse\x12*\n\x06\x64\x65lete\x12\x11.SessionIdRequest\x1a\r.SessionEmpty'
)




_SESSIONEMPTY = _descriptor.Descriptor(
  name='SessionEmpty',
  full_name='SessionEmpty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=31,
)


_SESSIONIDREQUEST = _descriptor.Descriptor(
  name='SessionIdRequest',
  full_name='SessionIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SessionIdRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=63,
)


_SESSIONONEREQUEST = _descriptor.Descriptor(
  name='SessionOneRequest',
  full_name='SessionOneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userAgent', full_name='SessionOneRequest.userAgent', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='SessionOneRequest.ip', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=115,
)


_SESSIONNOTIDREQUEST = _descriptor.Descriptor(
  name='SessionNotIdRequest',
  full_name='SessionNotIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='SessionNotIdRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app', full_name='SessionNotIdRequest.app', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='SessionNotIdRequest.ip', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='SessionNotIdRequest.location', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userAgent', full_name='SessionNotIdRequest.userAgent', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid', full_name='SessionNotIdRequest.valid', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='SessionNotIdRequest.active', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=246,
)


_SESSIONREQUEST = _descriptor.Descriptor(
  name='SessionRequest',
  full_name='SessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SessionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='SessionRequest.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app', full_name='SessionRequest.app', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='SessionRequest.ip', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='SessionRequest.location', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userAgent', full_name='SessionRequest.userAgent', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid', full_name='SessionRequest.valid', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='SessionRequest.active', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=384,
)


_SESSIONTABLEREQUEST = _descriptor.Descriptor(
  name='SessionTableRequest',
  full_name='SessionTableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='SessionTableRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='SessionTableRequest.per_page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=15,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='search', full_name='SessionTableRequest.search', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=459,
)


_SESSIONRESPONSE = _descriptor.Descriptor(
  name='SessionResponse',
  full_name='SessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='SessionResponse.session', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=512,
)


_SESSIONMULTIPLERESPONSE = _descriptor.Descriptor(
  name='SessionMultipleResponse',
  full_name='SessionMultipleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='SessionMultipleResponse.session', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=573,
)


_SESSIONTABLERESPONSE = _descriptor.Descriptor(
  name='SessionTableResponse',
  full_name='SessionTableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='SessionTableResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='SessionTableResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='SessionTableResponse.per_page', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_items', full_name='SessionTableResponse.total_items', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_pages', full_name='SessionTableResponse.num_pages', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=575,
  serialized_end=701,
)

_SESSIONRESPONSE.fields_by_name['session'].message_type = _SESSIONREQUEST
_SESSIONMULTIPLERESPONSE.fields_by_name['session'].message_type = _SESSIONREQUEST
_SESSIONTABLERESPONSE.fields_by_name['items'].message_type = _SESSIONREQUEST
DESCRIPTOR.message_types_by_name['SessionEmpty'] = _SESSIONEMPTY
DESCRIPTOR.message_types_by_name['SessionIdRequest'] = _SESSIONIDREQUEST
DESCRIPTOR.message_types_by_name['SessionOneRequest'] = _SESSIONONEREQUEST
DESCRIPTOR.message_types_by_name['SessionNotIdRequest'] = _SESSIONNOTIDREQUEST
DESCRIPTOR.message_types_by_name['SessionRequest'] = _SESSIONREQUEST
DESCRIPTOR.message_types_by_name['SessionTableRequest'] = _SESSIONTABLEREQUEST
DESCRIPTOR.message_types_by_name['SessionResponse'] = _SESSIONRESPONSE
DESCRIPTOR.message_types_by_name['SessionMultipleResponse'] = _SESSIONMULTIPLERESPONSE
DESCRIPTOR.message_types_by_name['SessionTableResponse'] = _SESSIONTABLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionEmpty = _reflection.GeneratedProtocolMessageType('SessionEmpty', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONEMPTY,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionEmpty)
  })
_sym_db.RegisterMessage(SessionEmpty)

SessionIdRequest = _reflection.GeneratedProtocolMessageType('SessionIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONIDREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionIdRequest)
  })
_sym_db.RegisterMessage(SessionIdRequest)

SessionOneRequest = _reflection.GeneratedProtocolMessageType('SessionOneRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONONEREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionOneRequest)
  })
_sym_db.RegisterMessage(SessionOneRequest)

SessionNotIdRequest = _reflection.GeneratedProtocolMessageType('SessionNotIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONNOTIDREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionNotIdRequest)
  })
_sym_db.RegisterMessage(SessionNotIdRequest)

SessionRequest = _reflection.GeneratedProtocolMessageType('SessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionRequest)
  })
_sym_db.RegisterMessage(SessionRequest)

SessionTableRequest = _reflection.GeneratedProtocolMessageType('SessionTableRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONTABLEREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionTableRequest)
  })
_sym_db.RegisterMessage(SessionTableRequest)

SessionResponse = _reflection.GeneratedProtocolMessageType('SessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONRESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionResponse)
  })
_sym_db.RegisterMessage(SessionResponse)

SessionMultipleResponse = _reflection.GeneratedProtocolMessageType('SessionMultipleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONMULTIPLERESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionMultipleResponse)
  })
_sym_db.RegisterMessage(SessionMultipleResponse)

SessionTableResponse = _reflection.GeneratedProtocolMessageType('SessionTableResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONTABLERESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:SessionTableResponse)
  })
_sym_db.RegisterMessage(SessionTableResponse)



_SESSION = _descriptor.ServiceDescriptor(
  name='Session',
  full_name='Session',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=704,
  serialized_end=1001,
  methods=[
  _descriptor.MethodDescriptor(
    name='table',
    full_name='Session.table',
    index=0,
    containing_service=None,
    input_type=_SESSIONTABLEREQUEST,
    output_type=_SESSIONTABLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_all',
    full_name='Session.get_all',
    index=1,
    containing_service=None,
    input_type=_SESSIONEMPTY,
    output_type=_SESSIONMULTIPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='Session.get',
    index=2,
    containing_service=None,
    input_type=_SESSIONONEREQUEST,
    output_type=_SESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='save',
    full_name='Session.save',
    index=3,
    containing_service=None,
    input_type=_SESSIONNOTIDREQUEST,
    output_type=_SESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='Session.update',
    index=4,
    containing_service=None,
    input_type=_SESSIONREQUEST,
    output_type=_SESSIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='Session.delete',
    index=5,
    containing_service=None,
    input_type=_SESSIONIDREQUEST,
    output_type=_SESSIONEMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSION)

DESCRIPTOR.services_by_name['Session'] = _SESSION

# @@protoc_insertion_point(module_scope)
