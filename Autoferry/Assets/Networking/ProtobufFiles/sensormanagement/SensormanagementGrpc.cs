// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: sensormanagement/sensormanagement.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Sensormanagement {
  /// <summary>
  /// The data service definition
  /// </summary>
  public static partial class SensorManagement
  {
    static readonly string __ServiceName = "sensormanagement.SensorManagement";

    static readonly grpc::Marshaller<global::Sensormanagement.StartRenderingRequest> __Marshaller_sensormanagement_StartRenderingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.StartRenderingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.StartRenderingResponse> __Marshaller_sensormanagement_StartRenderingResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.StartRenderingResponse.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.StopRenderingRequest> __Marshaller_sensormanagement_StopRenderingRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.StopRenderingRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.StopRenderingResponse> __Marshaller_sensormanagement_StopRenderingResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.StopRenderingResponse.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.AllSensorsOfTypeRequest> __Marshaller_sensormanagement_AllSensorsOfTypeRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.AllSensorsOfTypeRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.AllSensorsOfTypeResponse> __Marshaller_sensormanagement_AllSensorsOfTypeResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.AllSensorsOfTypeResponse.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.AllSensorsOnVesselRequest> __Marshaller_sensormanagement_AllSensorsOnVesselRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.AllSensorsOnVesselRequest.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::Sensormanagement.AllSensorsOnVesselResponse> __Marshaller_sensormanagement_AllSensorsOnVesselResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::Sensormanagement.AllSensorsOnVesselResponse.Parser.ParseFrom);

    static readonly grpc::Method<global::Sensormanagement.StartRenderingRequest, global::Sensormanagement.StartRenderingResponse> __Method_StartRendering = new grpc::Method<global::Sensormanagement.StartRenderingRequest, global::Sensormanagement.StartRenderingResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "StartRendering",
        __Marshaller_sensormanagement_StartRenderingRequest,
        __Marshaller_sensormanagement_StartRenderingResponse);

    static readonly grpc::Method<global::Sensormanagement.StopRenderingRequest, global::Sensormanagement.StopRenderingResponse> __Method_StopRendering = new grpc::Method<global::Sensormanagement.StopRenderingRequest, global::Sensormanagement.StopRenderingResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "StopRendering",
        __Marshaller_sensormanagement_StopRenderingRequest,
        __Marshaller_sensormanagement_StopRenderingResponse);

    static readonly grpc::Method<global::Sensormanagement.AllSensorsOfTypeRequest, global::Sensormanagement.AllSensorsOfTypeResponse> __Method_GetAllSensorsOfType = new grpc::Method<global::Sensormanagement.AllSensorsOfTypeRequest, global::Sensormanagement.AllSensorsOfTypeResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetAllSensorsOfType",
        __Marshaller_sensormanagement_AllSensorsOfTypeRequest,
        __Marshaller_sensormanagement_AllSensorsOfTypeResponse);

    static readonly grpc::Method<global::Sensormanagement.AllSensorsOnVesselRequest, global::Sensormanagement.AllSensorsOnVesselResponse> __Method_GetAllSensorsOnVessel = new grpc::Method<global::Sensormanagement.AllSensorsOnVesselRequest, global::Sensormanagement.AllSensorsOnVesselResponse>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetAllSensorsOnVessel",
        __Marshaller_sensormanagement_AllSensorsOnVesselRequest,
        __Marshaller_sensormanagement_AllSensorsOnVesselResponse);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Sensormanagement.SensormanagementReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of SensorManagement</summary>
    [grpc::BindServiceMethod(typeof(SensorManagement), "BindService")]
    public abstract partial class SensorManagementBase
    {
      public virtual global::System.Threading.Tasks.Task<global::Sensormanagement.StartRenderingResponse> StartRendering(global::Sensormanagement.StartRenderingRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Sensormanagement.StopRenderingResponse> StopRendering(global::Sensormanagement.StopRenderingRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Sensormanagement.AllSensorsOfTypeResponse> GetAllSensorsOfType(global::Sensormanagement.AllSensorsOfTypeRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Sensormanagement.AllSensorsOnVesselResponse> GetAllSensorsOnVessel(global::Sensormanagement.AllSensorsOnVesselRequest request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for SensorManagement</summary>
    public partial class SensorManagementClient : grpc::ClientBase<SensorManagementClient>
    {
      /// <summary>Creates a new client for SensorManagement</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public SensorManagementClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for SensorManagement that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public SensorManagementClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected SensorManagementClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected SensorManagementClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::Sensormanagement.StartRenderingResponse StartRendering(global::Sensormanagement.StartRenderingRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StartRendering(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Sensormanagement.StartRenderingResponse StartRendering(global::Sensormanagement.StartRenderingRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_StartRendering, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.StartRenderingResponse> StartRenderingAsync(global::Sensormanagement.StartRenderingRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StartRenderingAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.StartRenderingResponse> StartRenderingAsync(global::Sensormanagement.StartRenderingRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_StartRendering, null, options, request);
      }
      public virtual global::Sensormanagement.StopRenderingResponse StopRendering(global::Sensormanagement.StopRenderingRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StopRendering(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Sensormanagement.StopRenderingResponse StopRendering(global::Sensormanagement.StopRenderingRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_StopRendering, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.StopRenderingResponse> StopRenderingAsync(global::Sensormanagement.StopRenderingRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StopRenderingAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.StopRenderingResponse> StopRenderingAsync(global::Sensormanagement.StopRenderingRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_StopRendering, null, options, request);
      }
      public virtual global::Sensormanagement.AllSensorsOfTypeResponse GetAllSensorsOfType(global::Sensormanagement.AllSensorsOfTypeRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetAllSensorsOfType(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Sensormanagement.AllSensorsOfTypeResponse GetAllSensorsOfType(global::Sensormanagement.AllSensorsOfTypeRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetAllSensorsOfType, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.AllSensorsOfTypeResponse> GetAllSensorsOfTypeAsync(global::Sensormanagement.AllSensorsOfTypeRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetAllSensorsOfTypeAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.AllSensorsOfTypeResponse> GetAllSensorsOfTypeAsync(global::Sensormanagement.AllSensorsOfTypeRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetAllSensorsOfType, null, options, request);
      }
      public virtual global::Sensormanagement.AllSensorsOnVesselResponse GetAllSensorsOnVessel(global::Sensormanagement.AllSensorsOnVesselRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetAllSensorsOnVessel(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Sensormanagement.AllSensorsOnVesselResponse GetAllSensorsOnVessel(global::Sensormanagement.AllSensorsOnVesselRequest request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetAllSensorsOnVessel, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.AllSensorsOnVesselResponse> GetAllSensorsOnVesselAsync(global::Sensormanagement.AllSensorsOnVesselRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetAllSensorsOnVesselAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Sensormanagement.AllSensorsOnVesselResponse> GetAllSensorsOnVesselAsync(global::Sensormanagement.AllSensorsOnVesselRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetAllSensorsOnVessel, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override SensorManagementClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new SensorManagementClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(SensorManagementBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_StartRendering, serviceImpl.StartRendering)
          .AddMethod(__Method_StopRendering, serviceImpl.StopRendering)
          .AddMethod(__Method_GetAllSensorsOfType, serviceImpl.GetAllSensorsOfType)
          .AddMethod(__Method_GetAllSensorsOnVessel, serviceImpl.GetAllSensorsOnVessel).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, SensorManagementBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_StartRendering, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Sensormanagement.StartRenderingRequest, global::Sensormanagement.StartRenderingResponse>(serviceImpl.StartRendering));
      serviceBinder.AddMethod(__Method_StopRendering, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Sensormanagement.StopRenderingRequest, global::Sensormanagement.StopRenderingResponse>(serviceImpl.StopRendering));
      serviceBinder.AddMethod(__Method_GetAllSensorsOfType, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Sensormanagement.AllSensorsOfTypeRequest, global::Sensormanagement.AllSensorsOfTypeResponse>(serviceImpl.GetAllSensorsOfType));
      serviceBinder.AddMethod(__Method_GetAllSensorsOnVessel, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Sensormanagement.AllSensorsOnVesselRequest, global::Sensormanagement.AllSensorsOnVesselResponse>(serviceImpl.GetAllSensorsOnVessel));
    }

  }
}
#endregion
