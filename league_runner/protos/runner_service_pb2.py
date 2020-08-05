# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runner_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='runner_service.proto',
  package='rlleague',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14runner_service.proto\x12\x08rlleague\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0c\x63ommon.proto\"(\n\x0c\x41gentRequest\x12\x18\n\x10number_of_agents\x18\x01 \x01(\x05\"5\n\rAgentResponse\x12\x16\n\x06\x61gents\x18\x01 \x03(\x0b\x32\x06.Agent\x12\x0c\n\x04uuid\x18\x02 \x01(\x03\"\x1b\n\x0bGameRequest\x12\x0c\n\x04uuid\x18\x02 \x01(\x03\"$\n\x0cGameResponse\x12\x14\n\x05games\x18\x01 \x03(\x0b\x32\x05.Game\"-\n\rReportRequest\x12\x1c\n\x07results\x18\x01 \x03(\x0b\x32\x0b.GameResult2\xd8\x01\n\x0cLeagueRunner\x12\x43\n\x0eRequeustAgents\x12\x16.rlleague.AgentRequest\x1a\x17.rlleague.AgentResponse\"\x00\x12?\n\x0cRequestGames\x12\x15.rlleague.GameRequest\x1a\x16.rlleague.GameResponse\"\x00\x12\x42\n\rReportResults\x12\x17.rlleague.ReportRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])




_AGENTREQUEST = _descriptor.Descriptor(
  name='AgentRequest',
  full_name='rlleague.AgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_of_agents', full_name='rlleague.AgentRequest.number_of_agents', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=117,
)


_AGENTRESPONSE = _descriptor.Descriptor(
  name='AgentResponse',
  full_name='rlleague.AgentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='rlleague.AgentResponse.agents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='rlleague.AgentResponse.uuid', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=172,
)


_GAMEREQUEST = _descriptor.Descriptor(
  name='GameRequest',
  full_name='rlleague.GameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='rlleague.GameRequest.uuid', index=0,
      number=2, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=201,
)


_GAMERESPONSE = _descriptor.Descriptor(
  name='GameResponse',
  full_name='rlleague.GameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='games', full_name='rlleague.GameResponse.games', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=239,
)


_REPORTREQUEST = _descriptor.Descriptor(
  name='ReportRequest',
  full_name='rlleague.ReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='rlleague.ReportRequest.results', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=286,
)

_AGENTRESPONSE.fields_by_name['agents'].message_type = common__pb2._AGENT
_GAMERESPONSE.fields_by_name['games'].message_type = common__pb2._GAME
_REPORTREQUEST.fields_by_name['results'].message_type = common__pb2._GAMERESULT
DESCRIPTOR.message_types_by_name['AgentRequest'] = _AGENTREQUEST
DESCRIPTOR.message_types_by_name['AgentResponse'] = _AGENTRESPONSE
DESCRIPTOR.message_types_by_name['GameRequest'] = _GAMEREQUEST
DESCRIPTOR.message_types_by_name['GameResponse'] = _GAMERESPONSE
DESCRIPTOR.message_types_by_name['ReportRequest'] = _REPORTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentRequest = _reflection.GeneratedProtocolMessageType('AgentRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTREQUEST,
  '__module__' : 'runner_service_pb2'
  # @@protoc_insertion_point(class_scope:rlleague.AgentRequest)
  })
_sym_db.RegisterMessage(AgentRequest)

AgentResponse = _reflection.GeneratedProtocolMessageType('AgentResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTRESPONSE,
  '__module__' : 'runner_service_pb2'
  # @@protoc_insertion_point(class_scope:rlleague.AgentResponse)
  })
_sym_db.RegisterMessage(AgentResponse)

GameRequest = _reflection.GeneratedProtocolMessageType('GameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'runner_service_pb2'
  # @@protoc_insertion_point(class_scope:rlleague.GameRequest)
  })
_sym_db.RegisterMessage(GameRequest)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'runner_service_pb2'
  # @@protoc_insertion_point(class_scope:rlleague.GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)

ReportRequest = _reflection.GeneratedProtocolMessageType('ReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTREQUEST,
  '__module__' : 'runner_service_pb2'
  # @@protoc_insertion_point(class_scope:rlleague.ReportRequest)
  })
_sym_db.RegisterMessage(ReportRequest)



_LEAGUERUNNER = _descriptor.ServiceDescriptor(
  name='LeagueRunner',
  full_name='rlleague.LeagueRunner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=289,
  serialized_end=505,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequeustAgents',
    full_name='rlleague.LeagueRunner.RequeustAgents',
    index=0,
    containing_service=None,
    input_type=_AGENTREQUEST,
    output_type=_AGENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestGames',
    full_name='rlleague.LeagueRunner.RequestGames',
    index=1,
    containing_service=None,
    input_type=_GAMEREQUEST,
    output_type=_GAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportResults',
    full_name='rlleague.LeagueRunner.ReportResults',
    index=2,
    containing_service=None,
    input_type=_REPORTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEAGUERUNNER)

DESCRIPTOR.services_by_name['LeagueRunner'] = _LEAGUERUNNER

# @@protoc_insertion_point(module_scope)
