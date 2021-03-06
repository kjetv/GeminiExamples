# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from sensormanagement import sensormanagement_pb2 as sensormanagement_dot_sensormanagement__pb2


class SensorManagementStub(object):
  """The data service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartRendering = channel.unary_unary(
        '/sensormanagement.SensorManagement/StartRendering',
        request_serializer=sensormanagement_dot_sensormanagement__pb2.StartRenderingRequest.SerializeToString,
        response_deserializer=sensormanagement_dot_sensormanagement__pb2.StartRenderingResponse.FromString,
        )
    self.StopRendering = channel.unary_unary(
        '/sensormanagement.SensorManagement/StopRendering',
        request_serializer=sensormanagement_dot_sensormanagement__pb2.StopRenderingRequest.SerializeToString,
        response_deserializer=sensormanagement_dot_sensormanagement__pb2.StopRenderingResponse.FromString,
        )
    self.GetAllSensorsOfType = channel.unary_unary(
        '/sensormanagement.SensorManagement/GetAllSensorsOfType',
        request_serializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOfTypeRequest.SerializeToString,
        response_deserializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOfTypeResponse.FromString,
        )
    self.GetAllSensorsOnVessel = channel.unary_unary(
        '/sensormanagement.SensorManagement/GetAllSensorsOnVessel',
        request_serializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOnVesselRequest.SerializeToString,
        response_deserializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOnVesselResponse.FromString,
        )


class SensorManagementServicer(object):
  """The data service definition
  """

  def StartRendering(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopRendering(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllSensorsOfType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllSensorsOnVessel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SensorManagementServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartRendering': grpc.unary_unary_rpc_method_handler(
          servicer.StartRendering,
          request_deserializer=sensormanagement_dot_sensormanagement__pb2.StartRenderingRequest.FromString,
          response_serializer=sensormanagement_dot_sensormanagement__pb2.StartRenderingResponse.SerializeToString,
      ),
      'StopRendering': grpc.unary_unary_rpc_method_handler(
          servicer.StopRendering,
          request_deserializer=sensormanagement_dot_sensormanagement__pb2.StopRenderingRequest.FromString,
          response_serializer=sensormanagement_dot_sensormanagement__pb2.StopRenderingResponse.SerializeToString,
      ),
      'GetAllSensorsOfType': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllSensorsOfType,
          request_deserializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOfTypeRequest.FromString,
          response_serializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOfTypeResponse.SerializeToString,
      ),
      'GetAllSensorsOnVessel': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllSensorsOnVessel,
          request_deserializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOnVesselRequest.FromString,
          response_serializer=sensormanagement_dot_sensormanagement__pb2.AllSensorsOnVesselResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sensormanagement.SensorManagement', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
