# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: no_package_name.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='no_package_name.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\022./;no_package_name',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15no_package_name.proto\"\x05\n\x03Msg2\x19\n\x03Svc\x12\x12\n\x04Send\x12\x04.Msg\x1a\x04.MsgB\x14Z\x12./;no_package_nameb\x06proto3'
)




_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='Msg',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=30,
)

DESCRIPTOR.message_types_by_name['Msg'] = _MSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'no_package_name_pb2'
  # @@protoc_insertion_point(class_scope:Msg)
  })
_sym_db.RegisterMessage(Msg)


DESCRIPTOR._options = None

_SVC = _descriptor.ServiceDescriptor(
  name='Svc',
  full_name='Svc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=32,
  serialized_end=57,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='Svc.Send',
    index=0,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVC)

DESCRIPTOR.services_by_name['Svc'] = _SVC

# @@protoc_insertion_point(module_scope)
