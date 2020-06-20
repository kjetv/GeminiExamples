// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: sensordata/sensordata.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Sensordata {

  /// <summary>Holder for reflection information generated from sensordata/sensordata.proto</summary>
  public static partial class SensordataReflection {

    #region Descriptor
    /// <summary>File descriptor for sensordata/sensordata.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static SensordataReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChtzZW5zb3JkYXRhL3NlbnNvcmRhdGEucHJvdG8SCnNlbnNvcmRhdGEiJgoR",
            "U2Vuc29yZGF0YVJlcXVlc3QSEQoJb3BlcmF0aW9uGAEgASgJIjYKElNlbnNv",
            "cmRhdGFSZXNwb25zZRIMCgRkYXRhGAEgASgMEhIKCmRhdGFMZW5ndGgYAiAB",
            "KAUyugEKClNlbnNvcmRhdGESVQoSVHJhbnNmZXJTZW5zb3JkYXRhEh0uc2Vu",
            "c29yZGF0YS5TZW5zb3JkYXRhUmVxdWVzdBoeLnNlbnNvcmRhdGEuU2Vuc29y",
            "ZGF0YVJlc3BvbnNlIgASVQoQU3RyZWFtU2Vuc29yZGF0YRIdLnNlbnNvcmRh",
            "dGEuU2Vuc29yZGF0YVJlcXVlc3QaHi5zZW5zb3JkYXRhLlNlbnNvcmRhdGFS",
            "ZXNwb25zZSIAMAFCMQobaW8uZ3JwYy5leGFtcGxlcy5zZW5zb3JkYXRhQgpT",
            "ZW5zb3JkYXRhUAGiAgNITFdiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Sensordata.SensordataRequest), global::Sensordata.SensordataRequest.Parser, new[]{ "Operation" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Sensordata.SensordataResponse), global::Sensordata.SensordataResponse.Parser, new[]{ "Data", "DataLength" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  /// <summary>
  /// The requeset message containing the user's name.
  /// </summary>
  public sealed partial class SensordataRequest : pb::IMessage<SensordataRequest> {
    private static readonly pb::MessageParser<SensordataRequest> _parser = new pb::MessageParser<SensordataRequest>(() => new SensordataRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<SensordataRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Sensordata.SensordataReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SensordataRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SensordataRequest(SensordataRequest other) : this() {
      operation_ = other.operation_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SensordataRequest Clone() {
      return new SensordataRequest(this);
    }

    /// <summary>Field number for the "operation" field.</summary>
    public const int OperationFieldNumber = 1;
    private string operation_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Operation {
      get { return operation_; }
      set {
        operation_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as SensordataRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(SensordataRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Operation != other.Operation) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Operation.Length != 0) hash ^= Operation.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (Operation.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Operation);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Operation.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Operation);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(SensordataRequest other) {
      if (other == null) {
        return;
      }
      if (other.Operation.Length != 0) {
        Operation = other.Operation;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Operation = input.ReadString();
            break;
          }
        }
      }
    }

  }

  public sealed partial class SensordataResponse : pb::IMessage<SensordataResponse> {
    private static readonly pb::MessageParser<SensordataResponse> _parser = new pb::MessageParser<SensordataResponse>(() => new SensordataResponse());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<SensordataResponse> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Sensordata.SensordataReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SensordataResponse() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SensordataResponse(SensordataResponse other) : this() {
      data_ = other.data_;
      dataLength_ = other.dataLength_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public SensordataResponse Clone() {
      return new SensordataResponse(this);
    }

    /// <summary>Field number for the "data" field.</summary>
    public const int DataFieldNumber = 1;
    private pb::ByteString data_ = pb::ByteString.Empty;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public pb::ByteString Data {
      get { return data_; }
      set {
        data_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "dataLength" field.</summary>
    public const int DataLengthFieldNumber = 2;
    private int dataLength_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int DataLength {
      get { return dataLength_; }
      set {
        dataLength_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as SensordataResponse);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(SensordataResponse other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Data != other.Data) return false;
      if (DataLength != other.DataLength) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Data.Length != 0) hash ^= Data.GetHashCode();
      if (DataLength != 0) hash ^= DataLength.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (Data.Length != 0) {
        output.WriteRawTag(10);
        output.WriteBytes(Data);
      }
      if (DataLength != 0) {
        output.WriteRawTag(16);
        output.WriteInt32(DataLength);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Data.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeBytesSize(Data);
      }
      if (DataLength != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(DataLength);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(SensordataResponse other) {
      if (other == null) {
        return;
      }
      if (other.Data.Length != 0) {
        Data = other.Data;
      }
      if (other.DataLength != 0) {
        DataLength = other.DataLength;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            Data = input.ReadBytes();
            break;
          }
          case 16: {
            DataLength = input.ReadInt32();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code