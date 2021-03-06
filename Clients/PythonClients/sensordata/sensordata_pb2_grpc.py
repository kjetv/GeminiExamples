# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from sensordata import sensordata_pb2 as sensordata_dot_sensordata__pb2


class SensordataStub(object):
  """The data service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TransferSensordata = channel.unary_unary(
        '/sensordata.Sensordata/TransferSensordata',
        request_serializer=sensordata_dot_sensordata__pb2.SensordataRequest.SerializeToString,
        response_deserializer=sensordata_dot_sensordata__pb2.SensordataResponse.FromString,
        )
    self.StreamSensordata = channel.unary_stream(
        '/sensordata.Sensordata/StreamSensordata',
        request_serializer=sensordata_dot_sensordata__pb2.SensordataRequest.SerializeToString,
        response_deserializer=sensordata_dot_sensordata__pb2.SensordataResponse.FromString,
        )


class SensordataServicer(object):
  """The data service definition
  """

  def TransferSensordata(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamSensordata(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SensordataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TransferSensordata': grpc.unary_unary_rpc_method_handler(
          servicer.TransferSensordata,
          request_deserializer=sensordata_dot_sensordata__pb2.SensordataRequest.FromString,
          response_serializer=sensordata_dot_sensordata__pb2.SensordataResponse.SerializeToString,
      ),
      'StreamSensordata': grpc.unary_stream_rpc_method_handler(
          servicer.StreamSensordata,
          request_deserializer=sensordata_dot_sensordata__pb2.SensordataRequest.FromString,
          response_serializer=sensordata_dot_sensordata__pb2.SensordataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sensordata.Sensordata', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
