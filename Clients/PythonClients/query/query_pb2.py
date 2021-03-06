# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query/query.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='query/query.proto',
  package='query',
  syntax='proto3',
  serialized_options=_b('\n\024io.grpc.examples.apiB\005QueryP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x11query/query.proto\x12\x05query\"\'\n\x04Vec3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"\x92\x01\n\x06\x42ounds\x12\x1b\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x0b.query.Vec3\x12\x1c\n\x07\x65xtents\x18\x02 \x01(\x0b\x32\x0b.query.Vec3\x12\x18\n\x03max\x18\x03 \x01(\x0b\x32\x0b.query.Vec3\x12\x18\n\x03min\x18\x04 \x01(\x0b\x32\x0b.query.Vec3\x12\x19\n\x04size\x18\x05 \x01(\x0b\x32\x0b.query.Vec3\"\'\n\x13VesselBoundsRequest\x12\x10\n\x08vesselId\x18\x01 \x01(\t\"5\n\x14VesselBoundsResponse\x12\x1d\n\x06\x62ounds\x18\x01 \x01(\x0b\x32\r.query.Bounds\"#\n\x13\x41llVesselIdsRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\"#\n\x14\x41llVesselIdsResponse\x12\x0b\n\x03ids\x18\x01 \x03(\t\"\x1e\n\nIMURequest\x12\x10\n\x08vesselId\x18\x01 \x01(\t\"\x8d\x01\n\x0bIMUResponse\x12\x1d\n\x08position\x18\x01 \x01(\x0b\x32\x0b.query.Vec3\x12\x1d\n\x08velocity\x18\x02 \x01(\x0b\x32\x0b.query.Vec3\x12$\n\x0f\x61ngularVelocity\x18\x03 \x01(\x0b\x32\x0b.query.Vec3\x12\x1a\n\x05\x61ngle\x18\x04 \x01(\x0b\x32\x0b.query.Vec32\xe3\x01\n\x0cQueryService\x12L\n\x0fGetAllVesselIds\x12\x1a.query.AllVesselIdsRequest\x1a\x1b.query.AllVesselIdsResponse\"\x00\x12\x37\n\x0cGetVesselIMU\x12\x11.query.IMURequest\x1a\x12.query.IMUResponse\"\x00\x12L\n\x0fGetVesselBounds\x12\x1a.query.VesselBoundsRequest\x1a\x1b.query.VesselBoundsResponse\"\x00\x42%\n\x14io.grpc.examples.apiB\x05QueryP\x01\xa2\x02\x03HLWb\x06proto3')
)




_VEC3 = _descriptor.Descriptor(
  name='Vec3',
  full_name='query.Vec3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='query.Vec3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='query.Vec3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='query.Vec3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=28,
  serialized_end=67,
)


_BOUNDS = _descriptor.Descriptor(
  name='Bounds',
  full_name='query.Bounds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='center', full_name='query.Bounds.center', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extents', full_name='query.Bounds.extents', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='query.Bounds.max', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='query.Bounds.min', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='query.Bounds.size', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=70,
  serialized_end=216,
)


_VESSELBOUNDSREQUEST = _descriptor.Descriptor(
  name='VesselBoundsRequest',
  full_name='query.VesselBoundsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vesselId', full_name='query.VesselBoundsRequest.vesselId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=218,
  serialized_end=257,
)


_VESSELBOUNDSRESPONSE = _descriptor.Descriptor(
  name='VesselBoundsResponse',
  full_name='query.VesselBoundsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounds', full_name='query.VesselBoundsResponse.bounds', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=259,
  serialized_end=312,
)


_ALLVESSELIDSREQUEST = _descriptor.Descriptor(
  name='AllVesselIdsRequest',
  full_name='query.AllVesselIdsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='query.AllVesselIdsRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=314,
  serialized_end=349,
)


_ALLVESSELIDSRESPONSE = _descriptor.Descriptor(
  name='AllVesselIdsResponse',
  full_name='query.AllVesselIdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='query.AllVesselIdsResponse.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=351,
  serialized_end=386,
)


_IMUREQUEST = _descriptor.Descriptor(
  name='IMURequest',
  full_name='query.IMURequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vesselId', full_name='query.IMURequest.vesselId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=388,
  serialized_end=418,
)


_IMURESPONSE = _descriptor.Descriptor(
  name='IMUResponse',
  full_name='query.IMUResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='query.IMUResponse.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='query.IMUResponse.velocity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularVelocity', full_name='query.IMUResponse.angularVelocity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle', full_name='query.IMUResponse.angle', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=421,
  serialized_end=562,
)

_BOUNDS.fields_by_name['center'].message_type = _VEC3
_BOUNDS.fields_by_name['extents'].message_type = _VEC3
_BOUNDS.fields_by_name['max'].message_type = _VEC3
_BOUNDS.fields_by_name['min'].message_type = _VEC3
_BOUNDS.fields_by_name['size'].message_type = _VEC3
_VESSELBOUNDSRESPONSE.fields_by_name['bounds'].message_type = _BOUNDS
_IMURESPONSE.fields_by_name['position'].message_type = _VEC3
_IMURESPONSE.fields_by_name['velocity'].message_type = _VEC3
_IMURESPONSE.fields_by_name['angularVelocity'].message_type = _VEC3
_IMURESPONSE.fields_by_name['angle'].message_type = _VEC3
DESCRIPTOR.message_types_by_name['Vec3'] = _VEC3
DESCRIPTOR.message_types_by_name['Bounds'] = _BOUNDS
DESCRIPTOR.message_types_by_name['VesselBoundsRequest'] = _VESSELBOUNDSREQUEST
DESCRIPTOR.message_types_by_name['VesselBoundsResponse'] = _VESSELBOUNDSRESPONSE
DESCRIPTOR.message_types_by_name['AllVesselIdsRequest'] = _ALLVESSELIDSREQUEST
DESCRIPTOR.message_types_by_name['AllVesselIdsResponse'] = _ALLVESSELIDSRESPONSE
DESCRIPTOR.message_types_by_name['IMURequest'] = _IMUREQUEST
DESCRIPTOR.message_types_by_name['IMUResponse'] = _IMURESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vec3 = _reflection.GeneratedProtocolMessageType('Vec3', (_message.Message,), {
  'DESCRIPTOR' : _VEC3,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.Vec3)
  })
_sym_db.RegisterMessage(Vec3)

Bounds = _reflection.GeneratedProtocolMessageType('Bounds', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDS,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.Bounds)
  })
_sym_db.RegisterMessage(Bounds)

VesselBoundsRequest = _reflection.GeneratedProtocolMessageType('VesselBoundsRequest', (_message.Message,), {
  'DESCRIPTOR' : _VESSELBOUNDSREQUEST,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.VesselBoundsRequest)
  })
_sym_db.RegisterMessage(VesselBoundsRequest)

VesselBoundsResponse = _reflection.GeneratedProtocolMessageType('VesselBoundsResponse', (_message.Message,), {
  'DESCRIPTOR' : _VESSELBOUNDSRESPONSE,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.VesselBoundsResponse)
  })
_sym_db.RegisterMessage(VesselBoundsResponse)

AllVesselIdsRequest = _reflection.GeneratedProtocolMessageType('AllVesselIdsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLVESSELIDSREQUEST,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.AllVesselIdsRequest)
  })
_sym_db.RegisterMessage(AllVesselIdsRequest)

AllVesselIdsResponse = _reflection.GeneratedProtocolMessageType('AllVesselIdsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLVESSELIDSRESPONSE,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.AllVesselIdsResponse)
  })
_sym_db.RegisterMessage(AllVesselIdsResponse)

IMURequest = _reflection.GeneratedProtocolMessageType('IMURequest', (_message.Message,), {
  'DESCRIPTOR' : _IMUREQUEST,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.IMURequest)
  })
_sym_db.RegisterMessage(IMURequest)

IMUResponse = _reflection.GeneratedProtocolMessageType('IMUResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMURESPONSE,
  '__module__' : 'query.query_pb2'
  # @@protoc_insertion_point(class_scope:query.IMUResponse)
  })
_sym_db.RegisterMessage(IMUResponse)


DESCRIPTOR._options = None

_QUERYSERVICE = _descriptor.ServiceDescriptor(
  name='QueryService',
  full_name='query.QueryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=565,
  serialized_end=792,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllVesselIds',
    full_name='query.QueryService.GetAllVesselIds',
    index=0,
    containing_service=None,
    input_type=_ALLVESSELIDSREQUEST,
    output_type=_ALLVESSELIDSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetVesselIMU',
    full_name='query.QueryService.GetVesselIMU',
    index=1,
    containing_service=None,
    input_type=_IMUREQUEST,
    output_type=_IMURESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetVesselBounds',
    full_name='query.QueryService.GetVesselBounds',
    index=2,
    containing_service=None,
    input_type=_VESSELBOUNDSREQUEST,
    output_type=_VESSELBOUNDSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYSERVICE)

DESCRIPTOR.services_by_name['QueryService'] = _QUERYSERVICE

# @@protoc_insertion_point(module_scope)
