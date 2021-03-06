# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from imu import imu_pb2 as imu_dot_imu__pb2


class IMUServiceStub(object):
  """The data service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.IntialSetup = channel.unary_unary(
        '/imu.IMUService/IntialSetup',
        request_serializer=imu_dot_imu__pb2.IntialVesselParamsRequest.SerializeToString,
        response_deserializer=imu_dot_imu__pb2.InitialSetupResponse.FromString,
        )
    self.TransferIMUData = channel.unary_unary(
        '/imu.IMUService/TransferIMUData',
        request_serializer=imu_dot_imu__pb2.IMURequest.SerializeToString,
        response_deserializer=imu_dot_imu__pb2.IMUResponse.FromString,
        )


class IMUServiceServicer(object):
  """The data service definition
  """

  def IntialSetup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransferIMUData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IMUServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'IntialSetup': grpc.unary_unary_rpc_method_handler(
          servicer.IntialSetup,
          request_deserializer=imu_dot_imu__pb2.IntialVesselParamsRequest.FromString,
          response_serializer=imu_dot_imu__pb2.InitialSetupResponse.SerializeToString,
      ),
      'TransferIMUData': grpc.unary_unary_rpc_method_handler(
          servicer.TransferIMUData,
          request_deserializer=imu_dot_imu__pb2.IMURequest.FromString,
          response_serializer=imu_dot_imu__pb2.IMUResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'imu.IMUService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
