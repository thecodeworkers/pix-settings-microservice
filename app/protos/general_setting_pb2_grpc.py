# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import general_setting_pb2 as general__setting__pb2


class GeneralSettingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.table = channel.unary_unary(
                '/GeneralSetting/table',
                request_serializer=general__setting__pb2.GeneralSettingTableRequest.SerializeToString,
                response_deserializer=general__setting__pb2.GeneralSettingTableResponse.FromString,
                )
        self.get_all = channel.unary_unary(
                '/GeneralSetting/get_all',
                request_serializer=general__setting__pb2.GeneralSettingEmpty.SerializeToString,
                response_deserializer=general__setting__pb2.GeneralSettingMultipleResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/GeneralSetting/get',
                request_serializer=general__setting__pb2.GeneralSettingIdRequest.SerializeToString,
                response_deserializer=general__setting__pb2.GeneralSettingResponse.FromString,
                )
        self.save = channel.unary_unary(
                '/GeneralSetting/save',
                request_serializer=general__setting__pb2.GeneralSettingNotIdRequest.SerializeToString,
                response_deserializer=general__setting__pb2.GeneralSettingResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/GeneralSetting/update',
                request_serializer=general__setting__pb2.GeneralSettingRequest.SerializeToString,
                response_deserializer=general__setting__pb2.GeneralSettingResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/GeneralSetting/delete',
                request_serializer=general__setting__pb2.GeneralSettingIdRequest.SerializeToString,
                response_deserializer=general__setting__pb2.GeneralSettingEmpty.FromString,
                )


class GeneralSettingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def table(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_all(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeneralSettingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'table': grpc.unary_unary_rpc_method_handler(
                    servicer.table,
                    request_deserializer=general__setting__pb2.GeneralSettingTableRequest.FromString,
                    response_serializer=general__setting__pb2.GeneralSettingTableResponse.SerializeToString,
            ),
            'get_all': grpc.unary_unary_rpc_method_handler(
                    servicer.get_all,
                    request_deserializer=general__setting__pb2.GeneralSettingEmpty.FromString,
                    response_serializer=general__setting__pb2.GeneralSettingMultipleResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=general__setting__pb2.GeneralSettingIdRequest.FromString,
                    response_serializer=general__setting__pb2.GeneralSettingResponse.SerializeToString,
            ),
            'save': grpc.unary_unary_rpc_method_handler(
                    servicer.save,
                    request_deserializer=general__setting__pb2.GeneralSettingNotIdRequest.FromString,
                    response_serializer=general__setting__pb2.GeneralSettingResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=general__setting__pb2.GeneralSettingRequest.FromString,
                    response_serializer=general__setting__pb2.GeneralSettingResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=general__setting__pb2.GeneralSettingIdRequest.FromString,
                    response_serializer=general__setting__pb2.GeneralSettingEmpty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GeneralSetting', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeneralSetting(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def table(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeneralSetting/table',
            general__setting__pb2.GeneralSettingTableRequest.SerializeToString,
            general__setting__pb2.GeneralSettingTableResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_all(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeneralSetting/get_all',
            general__setting__pb2.GeneralSettingEmpty.SerializeToString,
            general__setting__pb2.GeneralSettingMultipleResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeneralSetting/get',
            general__setting__pb2.GeneralSettingIdRequest.SerializeToString,
            general__setting__pb2.GeneralSettingResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeneralSetting/save',
            general__setting__pb2.GeneralSettingNotIdRequest.SerializeToString,
            general__setting__pb2.GeneralSettingResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeneralSetting/update',
            general__setting__pb2.GeneralSettingRequest.SerializeToString,
            general__setting__pb2.GeneralSettingResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GeneralSetting/delete',
            general__setting__pb2.GeneralSettingIdRequest.SerializeToString,
            general__setting__pb2.GeneralSettingEmpty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
