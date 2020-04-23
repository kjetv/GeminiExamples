# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from remotecontrol import remotecontrol_pb2 as remotecontrol_dot_remotecontrol__pb2


class RemoteControlStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ApplyForce = channel.unary_unary(
        '/remotecontrol.RemoteControl/ApplyForce',
        request_serializer=remotecontrol_dot_remotecontrol__pb2.ForceRequest.SerializeToString,
        response_deserializer=remotecontrol_dot_remotecontrol__pb2.ForceResponse.FromString,
        )


class RemoteControlServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ApplyForce(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RemoteControlServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ApplyForce': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyForce,
          request_deserializer=remotecontrol_dot_remotecontrol__pb2.ForceRequest.FromString,
          response_serializer=remotecontrol_dot_remotecontrol__pb2.ForceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'remotecontrol.RemoteControl', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))