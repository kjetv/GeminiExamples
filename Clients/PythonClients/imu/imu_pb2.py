# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imu/imu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imu/imu.proto',
  package='imu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rimu/imu.proto\x12\x03imu\"F\n\x19IntialVesselParamsRequest\x12\x1b\n\x0fintertialMatrix\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x0c\n\x04mass\x18\x02 \x01(\x02\"\'\n\x14InitialSetupResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"4\n\nIMURequest\x12\x12\n\x06\x66orces\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x12\n\x06torque\x18\x02 \x03(\x02\x42\x02\x10\x01\"i\n\x0bIMUResponse\x12\x14\n\x08position\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x14\n\x08velocity\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x1b\n\x0f\x61ngularVelocity\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x11\n\x05\x61ngle\x18\x04 \x03(\x02\x42\x02\x10\x01\x32\x90\x01\n\nIMUService\x12J\n\x0bIntialSetup\x12\x1e.imu.IntialVesselParamsRequest\x1a\x19.imu.InitialSetupResponse\"\x00\x12\x36\n\x0fTransferIMUData\x12\x0f.imu.IMURequest\x1a\x10.imu.IMUResponse\"\x00\x62\x06proto3')
)




_INTIALVESSELPARAMSREQUEST = _descriptor.Descriptor(
  name='IntialVesselParamsRequest',
  full_name='imu.IntialVesselParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='intertialMatrix', full_name='imu.IntialVesselParamsRequest.intertialMatrix', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mass', full_name='imu.IntialVesselParamsRequest.mass', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=22,
  serialized_end=92,
)


_INITIALSETUPRESPONSE = _descriptor.Descriptor(
  name='InitialSetupResponse',
  full_name='imu.InitialSetupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='imu.InitialSetupResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=94,
  serialized_end=133,
)


_IMUREQUEST = _descriptor.Descriptor(
  name='IMURequest',
  full_name='imu.IMURequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forces', full_name='imu.IMURequest.forces', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torque', full_name='imu.IMURequest.torque', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=135,
  serialized_end=187,
)


_IMURESPONSE = _descriptor.Descriptor(
  name='IMUResponse',
  full_name='imu.IMUResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='imu.IMUResponse.position', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='imu.IMUResponse.velocity', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularVelocity', full_name='imu.IMUResponse.angularVelocity', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle', full_name='imu.IMUResponse.angle', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=189,
  serialized_end=294,
)

DESCRIPTOR.message_types_by_name['IntialVesselParamsRequest'] = _INTIALVESSELPARAMSREQUEST
DESCRIPTOR.message_types_by_name['InitialSetupResponse'] = _INITIALSETUPRESPONSE
DESCRIPTOR.message_types_by_name['IMURequest'] = _IMUREQUEST
DESCRIPTOR.message_types_by_name['IMUResponse'] = _IMURESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IntialVesselParamsRequest = _reflection.GeneratedProtocolMessageType('IntialVesselParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _INTIALVESSELPARAMSREQUEST,
  '__module__' : 'imu.imu_pb2'
  # @@protoc_insertion_point(class_scope:imu.IntialVesselParamsRequest)
  })
_sym_db.RegisterMessage(IntialVesselParamsRequest)

InitialSetupResponse = _reflection.GeneratedProtocolMessageType('InitialSetupResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITIALSETUPRESPONSE,
  '__module__' : 'imu.imu_pb2'
  # @@protoc_insertion_point(class_scope:imu.InitialSetupResponse)
  })
_sym_db.RegisterMessage(InitialSetupResponse)

IMURequest = _reflection.GeneratedProtocolMessageType('IMURequest', (_message.Message,), {
  'DESCRIPTOR' : _IMUREQUEST,
  '__module__' : 'imu.imu_pb2'
  # @@protoc_insertion_point(class_scope:imu.IMURequest)
  })
_sym_db.RegisterMessage(IMURequest)

IMUResponse = _reflection.GeneratedProtocolMessageType('IMUResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMURESPONSE,
  '__module__' : 'imu.imu_pb2'
  # @@protoc_insertion_point(class_scope:imu.IMUResponse)
  })
_sym_db.RegisterMessage(IMUResponse)


_INTIALVESSELPARAMSREQUEST.fields_by_name['intertialMatrix']._options = None
_IMUREQUEST.fields_by_name['forces']._options = None
_IMUREQUEST.fields_by_name['torque']._options = None
_IMURESPONSE.fields_by_name['position']._options = None
_IMURESPONSE.fields_by_name['velocity']._options = None
_IMURESPONSE.fields_by_name['angularVelocity']._options = None
_IMURESPONSE.fields_by_name['angle']._options = None

_IMUSERVICE = _descriptor.ServiceDescriptor(
  name='IMUService',
  full_name='imu.IMUService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=297,
  serialized_end=441,
  methods=[
  _descriptor.MethodDescriptor(
    name='IntialSetup',
    full_name='imu.IMUService.IntialSetup',
    index=0,
    containing_service=None,
    input_type=_INTIALVESSELPARAMSREQUEST,
    output_type=_INITIALSETUPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferIMUData',
    full_name='imu.IMUService.TransferIMUData',
    index=1,
    containing_service=None,
    input_type=_IMUREQUEST,
    output_type=_IMURESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMUSERVICE)

DESCRIPTOR.services_by_name['IMUService'] = _IMUSERVICE

# @@protoc_insertion_point(module_scope)
