# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensormanagement/sensormanagement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensormanagement/sensormanagement.proto',
  package='sensormanagement',
  syntax='proto3',
  serialized_options=_b('\n!io.grpc.examples.sensormanagementB\020SensorManagementP\001\242\002\003HLW'),
  serialized_pb=_b('\n\'sensormanagement/sensormanagement.proto\x12\x10sensormanagement\")\n\x15StartRenderingRequest\x12\x10\n\x08sensorID\x18\x01 \x01(\x05\")\n\x16StartRenderingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"(\n\x14StopRenderingRequest\x12\x10\n\x08sensorID\x18\x01 \x01(\x05\"(\n\x15StopRenderingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"E\n\x17\x41llSensorsOfTypeRequest\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.sensormanagement.SensorType\"E\n\x18\x41llSensorsOfTypeResponse\x12)\n\x07sensors\x18\x01 \x03(\x0b\x32\x18.sensormanagement.Sensor\"-\n\x19\x41llSensorsOnVesselRequest\x12\x10\n\x08vesselID\x18\x01 \x01(\t\"G\n\x1a\x41llSensorsOnVesselResponse\x12)\n\x07sensors\x18\x01 \x03(\x0b\x32\x18.sensormanagement.Sensor\"\x8c\x01\n\x06Sensor\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x04type\x18\x02 \x01(\x0e\x32\x1c.sensormanagement.SensorType\x12\x13\n\x0bsensorWidth\x18\x03 \x01(\x05\x12\x14\n\x0csensorHeight\x18\x04 \x01(\x05\x12\x11\n\tipAddress\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05*J\n\nSensorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07OPTICAL\x10\x01\x12\x0c\n\x08INFRARED\x10\x02\x12\t\n\x05RADAR\x10\x03\x12\t\n\x05LIDAR\x10\x04\x32\xc3\x03\n\x10SensorManagement\x12\x65\n\x0eStartRendering\x12\'.sensormanagement.StartRenderingRequest\x1a(.sensormanagement.StartRenderingResponse\"\x00\x12\x62\n\rStopRendering\x12&.sensormanagement.StopRenderingRequest\x1a\'.sensormanagement.StopRenderingResponse\"\x00\x12n\n\x13GetAllSensorsOfType\x12).sensormanagement.AllSensorsOfTypeRequest\x1a*.sensormanagement.AllSensorsOfTypeResponse\"\x00\x12t\n\x15GetAllSensorsOnVessel\x12+.sensormanagement.AllSensorsOnVesselRequest\x1a,.sensormanagement.AllSensorsOnVesselResponse\"\x00\x42=\n!io.grpc.examples.sensormanagementB\x10SensorManagementP\x01\xa2\x02\x03HLWb\x06proto3')
)

_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='sensormanagement.SensorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTICAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFRARED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RADAR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=636,
  serialized_end=710,
)
_sym_db.RegisterEnumDescriptor(_SENSORTYPE)

SensorType = enum_type_wrapper.EnumTypeWrapper(_SENSORTYPE)
UNKNOWN = 0
OPTICAL = 1
INFRARED = 2
RADAR = 3
LIDAR = 4



_STARTRENDERINGREQUEST = _descriptor.Descriptor(
  name='StartRenderingRequest',
  full_name='sensormanagement.StartRenderingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensorID', full_name='sensormanagement.StartRenderingRequest.sensorID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=61,
  serialized_end=102,
)


_STARTRENDERINGRESPONSE = _descriptor.Descriptor(
  name='StartRenderingResponse',
  full_name='sensormanagement.StartRenderingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='sensormanagement.StartRenderingResponse.success', index=0,
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
  serialized_start=104,
  serialized_end=145,
)


_STOPRENDERINGREQUEST = _descriptor.Descriptor(
  name='StopRenderingRequest',
  full_name='sensormanagement.StopRenderingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensorID', full_name='sensormanagement.StopRenderingRequest.sensorID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=147,
  serialized_end=187,
)


_STOPRENDERINGRESPONSE = _descriptor.Descriptor(
  name='StopRenderingResponse',
  full_name='sensormanagement.StopRenderingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='sensormanagement.StopRenderingResponse.success', index=0,
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
  serialized_start=189,
  serialized_end=229,
)


_ALLSENSORSOFTYPEREQUEST = _descriptor.Descriptor(
  name='AllSensorsOfTypeRequest',
  full_name='sensormanagement.AllSensorsOfTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='sensormanagement.AllSensorsOfTypeRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=231,
  serialized_end=300,
)


_ALLSENSORSOFTYPERESPONSE = _descriptor.Descriptor(
  name='AllSensorsOfTypeResponse',
  full_name='sensormanagement.AllSensorsOfTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='sensormanagement.AllSensorsOfTypeResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=302,
  serialized_end=371,
)


_ALLSENSORSONVESSELREQUEST = _descriptor.Descriptor(
  name='AllSensorsOnVesselRequest',
  full_name='sensormanagement.AllSensorsOnVesselRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vesselID', full_name='sensormanagement.AllSensorsOnVesselRequest.vesselID', index=0,
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
  serialized_start=373,
  serialized_end=418,
)


_ALLSENSORSONVESSELRESPONSE = _descriptor.Descriptor(
  name='AllSensorsOnVesselResponse',
  full_name='sensormanagement.AllSensorsOnVesselResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='sensormanagement.AllSensorsOnVesselResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=420,
  serialized_end=491,
)


_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='sensormanagement.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sensormanagement.Sensor.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensormanagement.Sensor.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorWidth', full_name='sensormanagement.Sensor.sensorWidth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensorHeight', full_name='sensormanagement.Sensor.sensorHeight', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipAddress', full_name='sensormanagement.Sensor.ipAddress', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='sensormanagement.Sensor.port', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=494,
  serialized_end=634,
)

_ALLSENSORSOFTYPEREQUEST.fields_by_name['type'].enum_type = _SENSORTYPE
_ALLSENSORSOFTYPERESPONSE.fields_by_name['sensors'].message_type = _SENSOR
_ALLSENSORSONVESSELRESPONSE.fields_by_name['sensors'].message_type = _SENSOR
_SENSOR.fields_by_name['type'].enum_type = _SENSORTYPE
DESCRIPTOR.message_types_by_name['StartRenderingRequest'] = _STARTRENDERINGREQUEST
DESCRIPTOR.message_types_by_name['StartRenderingResponse'] = _STARTRENDERINGRESPONSE
DESCRIPTOR.message_types_by_name['StopRenderingRequest'] = _STOPRENDERINGREQUEST
DESCRIPTOR.message_types_by_name['StopRenderingResponse'] = _STOPRENDERINGRESPONSE
DESCRIPTOR.message_types_by_name['AllSensorsOfTypeRequest'] = _ALLSENSORSOFTYPEREQUEST
DESCRIPTOR.message_types_by_name['AllSensorsOfTypeResponse'] = _ALLSENSORSOFTYPERESPONSE
DESCRIPTOR.message_types_by_name['AllSensorsOnVesselRequest'] = _ALLSENSORSONVESSELREQUEST
DESCRIPTOR.message_types_by_name['AllSensorsOnVesselResponse'] = _ALLSENSORSONVESSELRESPONSE
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR
DESCRIPTOR.enum_types_by_name['SensorType'] = _SENSORTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartRenderingRequest = _reflection.GeneratedProtocolMessageType('StartRenderingRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTRENDERINGREQUEST,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.StartRenderingRequest)
  })
_sym_db.RegisterMessage(StartRenderingRequest)

StartRenderingResponse = _reflection.GeneratedProtocolMessageType('StartRenderingResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTRENDERINGRESPONSE,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.StartRenderingResponse)
  })
_sym_db.RegisterMessage(StartRenderingResponse)

StopRenderingRequest = _reflection.GeneratedProtocolMessageType('StopRenderingRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPRENDERINGREQUEST,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.StopRenderingRequest)
  })
_sym_db.RegisterMessage(StopRenderingRequest)

StopRenderingResponse = _reflection.GeneratedProtocolMessageType('StopRenderingResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRENDERINGRESPONSE,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.StopRenderingResponse)
  })
_sym_db.RegisterMessage(StopRenderingResponse)

AllSensorsOfTypeRequest = _reflection.GeneratedProtocolMessageType('AllSensorsOfTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLSENSORSOFTYPEREQUEST,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.AllSensorsOfTypeRequest)
  })
_sym_db.RegisterMessage(AllSensorsOfTypeRequest)

AllSensorsOfTypeResponse = _reflection.GeneratedProtocolMessageType('AllSensorsOfTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLSENSORSOFTYPERESPONSE,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.AllSensorsOfTypeResponse)
  })
_sym_db.RegisterMessage(AllSensorsOfTypeResponse)

AllSensorsOnVesselRequest = _reflection.GeneratedProtocolMessageType('AllSensorsOnVesselRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALLSENSORSONVESSELREQUEST,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.AllSensorsOnVesselRequest)
  })
_sym_db.RegisterMessage(AllSensorsOnVesselRequest)

AllSensorsOnVesselResponse = _reflection.GeneratedProtocolMessageType('AllSensorsOnVesselResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALLSENSORSONVESSELRESPONSE,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.AllSensorsOnVesselResponse)
  })
_sym_db.RegisterMessage(AllSensorsOnVesselResponse)

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), {
  'DESCRIPTOR' : _SENSOR,
  '__module__' : 'sensormanagement.sensormanagement_pb2'
  # @@protoc_insertion_point(class_scope:sensormanagement.Sensor)
  })
_sym_db.RegisterMessage(Sensor)


DESCRIPTOR._options = None

_SENSORMANAGEMENT = _descriptor.ServiceDescriptor(
  name='SensorManagement',
  full_name='sensormanagement.SensorManagement',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=713,
  serialized_end=1164,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartRendering',
    full_name='sensormanagement.SensorManagement.StartRendering',
    index=0,
    containing_service=None,
    input_type=_STARTRENDERINGREQUEST,
    output_type=_STARTRENDERINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopRendering',
    full_name='sensormanagement.SensorManagement.StopRendering',
    index=1,
    containing_service=None,
    input_type=_STOPRENDERINGREQUEST,
    output_type=_STOPRENDERINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllSensorsOfType',
    full_name='sensormanagement.SensorManagement.GetAllSensorsOfType',
    index=2,
    containing_service=None,
    input_type=_ALLSENSORSOFTYPEREQUEST,
    output_type=_ALLSENSORSOFTYPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllSensorsOnVessel',
    full_name='sensormanagement.SensorManagement.GetAllSensorsOnVessel',
    index=3,
    containing_service=None,
    input_type=_ALLSENSORSONVESSELREQUEST,
    output_type=_ALLSENSORSONVESSELRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENSORMANAGEMENT)

DESCRIPTOR.services_by_name['SensorManagement'] = _SENSORMANAGEMENT

# @@protoc_insertion_point(module_scope)
