# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: force/force.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='force/force.proto',
  package='force',
  syntax='proto3',
  serialized_options=_b('\n\026io.grpc.examples.forceB\005ForceP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x11\x66orce/force.proto\x12\x05\x66orce\"+\n\x08Position\x12\t\n\x01n\x18\x01 \x01(\x02\x12\t\n\x01\x65\x18\x02 \x01(\x02\x12\t\n\x01\x64\x18\x03 \x01(\x02\"6\n\x0bOrientation\x12\x0b\n\x03phi\x18\x01 \x01(\x02\x12\r\n\x05theta\x18\x02 \x01(\x02\x12\x0b\n\x03psi\x18\x03 \x01(\x02\"+\n\x08Velocity\x12\t\n\x01u\x18\x01 \x01(\x02\x12\t\n\x01v\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\"2\n\x0f\x41ngularVelocity\x12\t\n\x01p\x18\x01 \x01(\x02\x12\t\n\x01q\x18\x02 \x01(\x02\x12\t\n\x01r\x18\x03 \x01(\x02\";\n\x0c\x41\x63\x63\x65leration\x12\r\n\x05u_dot\x18\x01 \x01(\x02\x12\r\n\x05v_dot\x18\x02 \x01(\x02\x12\r\n\x05w_dot\x18\x03 \x01(\x02\"B\n\x13\x41ngularAcceleration\x12\r\n\x05p_dot\x18\x01 \x01(\x02\x12\r\n\x05q_dot\x18\x02 \x01(\x02\x12\r\n\x05r_dot\x18\x03 \x01(\x02\"T\n\x10GeneralizedForce\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01k\x18\x04 \x01(\x02\x12\t\n\x01m\x18\x05 \x01(\x02\x12\t\n\x01n\x18\x06 \x01(\x02\"S\n\x0c\x46orceRequest\x12\x10\n\x08vesselId\x18\x01 \x01(\t\x12\x31\n\x10generalizedForce\x18\x02 \x01(\x0b\x32\x17.force.GeneralizedForce\"\x93\x02\n\rForceResponse\x12!\n\x08position\x18\x01 \x01(\x0b\x32\x0f.force.Position\x12\'\n\x0borientation\x18\x02 \x01(\x0b\x32\x12.force.Orientation\x12!\n\x08velocity\x18\x03 \x01(\x0b\x32\x0f.force.Velocity\x12/\n\x0f\x61ngularVelocity\x18\x04 \x01(\x0b\x32\x16.force.AngularVelocity\x12)\n\x0c\x61\x63\x63\x65leration\x18\x05 \x01(\x0b\x32\x13.force.Acceleration\x12\x37\n\x13\x61ngularAcceleration\x18\x06 \x01(\x0b\x32\x1a.force.AngularAcceleration2B\n\x05\x46orce\x12\x39\n\nApplyForce\x12\x13.force.ForceRequest\x1a\x14.force.ForceResponse\"\x00\x42\'\n\x16io.grpc.examples.forceB\x05\x46orceP\x01\xa2\x02\x03HLWb\x06proto3')
)




_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='force.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='force.Position.n', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='e', full_name='force.Position.e', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='force.Position.d', index=2,
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
  serialized_end=71,
)


_ORIENTATION = _descriptor.Descriptor(
  name='Orientation',
  full_name='force.Orientation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phi', full_name='force.Orientation.phi', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theta', full_name='force.Orientation.theta', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='psi', full_name='force.Orientation.psi', index=2,
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
  serialized_start=73,
  serialized_end=127,
)


_VELOCITY = _descriptor.Descriptor(
  name='Velocity',
  full_name='force.Velocity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='u', full_name='force.Velocity.u', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v', full_name='force.Velocity.v', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='force.Velocity.w', index=2,
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
  serialized_start=129,
  serialized_end=172,
)


_ANGULARVELOCITY = _descriptor.Descriptor(
  name='AngularVelocity',
  full_name='force.AngularVelocity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p', full_name='force.AngularVelocity.p', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='force.AngularVelocity.q', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r', full_name='force.AngularVelocity.r', index=2,
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
  serialized_start=174,
  serialized_end=224,
)


_ACCELERATION = _descriptor.Descriptor(
  name='Acceleration',
  full_name='force.Acceleration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='u_dot', full_name='force.Acceleration.u_dot', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v_dot', full_name='force.Acceleration.v_dot', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w_dot', full_name='force.Acceleration.w_dot', index=2,
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
  serialized_start=226,
  serialized_end=285,
)


_ANGULARACCELERATION = _descriptor.Descriptor(
  name='AngularAcceleration',
  full_name='force.AngularAcceleration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_dot', full_name='force.AngularAcceleration.p_dot', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q_dot', full_name='force.AngularAcceleration.q_dot', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r_dot', full_name='force.AngularAcceleration.r_dot', index=2,
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
  serialized_start=287,
  serialized_end=353,
)


_GENERALIZEDFORCE = _descriptor.Descriptor(
  name='GeneralizedForce',
  full_name='force.GeneralizedForce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='force.GeneralizedForce.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='force.GeneralizedForce.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='force.GeneralizedForce.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='force.GeneralizedForce.k', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m', full_name='force.GeneralizedForce.m', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='force.GeneralizedForce.n', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=355,
  serialized_end=439,
)


_FORCEREQUEST = _descriptor.Descriptor(
  name='ForceRequest',
  full_name='force.ForceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vesselId', full_name='force.ForceRequest.vesselId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generalizedForce', full_name='force.ForceRequest.generalizedForce', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=441,
  serialized_end=524,
)


_FORCERESPONSE = _descriptor.Descriptor(
  name='ForceResponse',
  full_name='force.ForceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='force.ForceResponse.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='force.ForceResponse.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='force.ForceResponse.velocity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularVelocity', full_name='force.ForceResponse.angularVelocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='force.ForceResponse.acceleration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularAcceleration', full_name='force.ForceResponse.angularAcceleration', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=527,
  serialized_end=802,
)

_FORCEREQUEST.fields_by_name['generalizedForce'].message_type = _GENERALIZEDFORCE
_FORCERESPONSE.fields_by_name['position'].message_type = _POSITION
_FORCERESPONSE.fields_by_name['orientation'].message_type = _ORIENTATION
_FORCERESPONSE.fields_by_name['velocity'].message_type = _VELOCITY
_FORCERESPONSE.fields_by_name['angularVelocity'].message_type = _ANGULARVELOCITY
_FORCERESPONSE.fields_by_name['acceleration'].message_type = _ACCELERATION
_FORCERESPONSE.fields_by_name['angularAcceleration'].message_type = _ANGULARACCELERATION
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Orientation'] = _ORIENTATION
DESCRIPTOR.message_types_by_name['Velocity'] = _VELOCITY
DESCRIPTOR.message_types_by_name['AngularVelocity'] = _ANGULARVELOCITY
DESCRIPTOR.message_types_by_name['Acceleration'] = _ACCELERATION
DESCRIPTOR.message_types_by_name['AngularAcceleration'] = _ANGULARACCELERATION
DESCRIPTOR.message_types_by_name['GeneralizedForce'] = _GENERALIZEDFORCE
DESCRIPTOR.message_types_by_name['ForceRequest'] = _FORCEREQUEST
DESCRIPTOR.message_types_by_name['ForceResponse'] = _FORCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.Position)
  })
_sym_db.RegisterMessage(Position)

Orientation = _reflection.GeneratedProtocolMessageType('Orientation', (_message.Message,), {
  'DESCRIPTOR' : _ORIENTATION,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.Orientation)
  })
_sym_db.RegisterMessage(Orientation)

Velocity = _reflection.GeneratedProtocolMessageType('Velocity', (_message.Message,), {
  'DESCRIPTOR' : _VELOCITY,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.Velocity)
  })
_sym_db.RegisterMessage(Velocity)

AngularVelocity = _reflection.GeneratedProtocolMessageType('AngularVelocity', (_message.Message,), {
  'DESCRIPTOR' : _ANGULARVELOCITY,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.AngularVelocity)
  })
_sym_db.RegisterMessage(AngularVelocity)

Acceleration = _reflection.GeneratedProtocolMessageType('Acceleration', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATION,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.Acceleration)
  })
_sym_db.RegisterMessage(Acceleration)

AngularAcceleration = _reflection.GeneratedProtocolMessageType('AngularAcceleration', (_message.Message,), {
  'DESCRIPTOR' : _ANGULARACCELERATION,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.AngularAcceleration)
  })
_sym_db.RegisterMessage(AngularAcceleration)

GeneralizedForce = _reflection.GeneratedProtocolMessageType('GeneralizedForce', (_message.Message,), {
  'DESCRIPTOR' : _GENERALIZEDFORCE,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.GeneralizedForce)
  })
_sym_db.RegisterMessage(GeneralizedForce)

ForceRequest = _reflection.GeneratedProtocolMessageType('ForceRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORCEREQUEST,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.ForceRequest)
  })
_sym_db.RegisterMessage(ForceRequest)

ForceResponse = _reflection.GeneratedProtocolMessageType('ForceResponse', (_message.Message,), {
  'DESCRIPTOR' : _FORCERESPONSE,
  '__module__' : 'force.force_pb2'
  # @@protoc_insertion_point(class_scope:force.ForceResponse)
  })
_sym_db.RegisterMessage(ForceResponse)


DESCRIPTOR._options = None

_FORCE = _descriptor.ServiceDescriptor(
  name='Force',
  full_name='force.Force',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=804,
  serialized_end=870,
  methods=[
  _descriptor.MethodDescriptor(
    name='ApplyForce',
    full_name='force.Force.ApplyForce',
    index=0,
    containing_service=None,
    input_type=_FORCEREQUEST,
    output_type=_FORCERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORCE)

DESCRIPTOR.services_by_name['Force'] = _FORCE

# @@protoc_insertion_point(module_scope)
