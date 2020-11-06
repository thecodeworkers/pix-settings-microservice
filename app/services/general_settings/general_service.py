from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import general_setting_pb2, general_setting_pb2_grpc
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from ...models import GeneralSettings


class GeneralSettingService(general_setting_pb2_grpc.GeneralSettingServicer):
    def table(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_general_setting_table')

            general_settings = GeneralSettings.objects

            response = paginate(general_settings, request.page, request.per_page)

            response = general_setting_pb2.GeneralSettingTableResponse(**response)

            return response

        except Exception as error:
            raise Exception(error)

    def get_all(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_general_setting_get_all')

            general_settings = parser_all_object(GeneralSettings.objects.all())
            response = general_setting_pb2.GeneralSettingMultipleResponse(general=general_settings)
        except Exception as error:
            raise Exception(error)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_general_setting_get')

            general_setting = GeneralSettings.objects.get(id=request.id)
            general_setting = parser_one_object(general_setting)
            response = general_setting_pb2.GeneralSettingResponse(general=general_setting)

            return response

        except GeneralSettings.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_general_setting_save')

            general_setting_object = MessageToDict(request)

            general_setting = GeneralSettings(**general_setting_object)
            general_setting.save()

            general_setting = parser_one_object(general_setting)

            response = general_setting_pb2.GeneralSettingResponse(general=general_setting)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_general_setting_update')

            general_setting_object = MessageToDict(request)
            general_setting = GeneralSettings.objects.get(id=general_setting_object['id'])


            if general_setting:
                del general_setting_object['id']

            general_setting.update(**general_setting_object)

            general_setting = GeneralSettings.objects.get(id=general_setting.id)

            general_setting = parser_one_object(general_setting)
            response = general_setting_pb2.GeneralSettingResponse(general=general_setting)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_general_setting_delete')

            general_setting = GeneralSettings.objects.get(id=request.id)
            general_setting = general_setting.delete()

            response = general_setting_pb2.GeneralSettingEmpty()

            return response

        except GeneralSettings.DoesNotExist as e:
            not_exist_code(context, e)


def start_general_setting_service():
    general_setting_pb2_grpc.add_GeneralSettingServicer_to_server(GeneralSettingService(), grpc_server)
