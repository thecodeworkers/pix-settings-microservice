from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import business_setting_pb2, business_setting_pb2_grpc
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from ...models import BusinessSettings


class BusinessSettingService(business_setting_pb2_grpc.BusinessSettingServicer):
    def table(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_business_setting_table')

            business_settings = BusinessSettings.objects

            response = paginate(business_settings, request.page, request.per_page)

            response = business_setting_pb2.BusinessSettingTableResponse(**response)

            return response

        except Exception as error:
            raise Exception(error)

    def get_all(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_business_setting_get_all')

            business_settings = parser_all_object(BusinessSettings.objects.all())
            response = business_setting_pb2.BusinessSettingMultipleResponse(business=business_settings)
        except Exception as error:
            raise Exception(error)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_business_setting_get')

            business_setting = BusinessSettings.objects.get(id=request.id)
            business_setting = parser_one_object(business_setting)
            response = business_setting_pb2.BusinessSettingResponse(business=business_setting)

            return response

        except BusinessSettings.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_business_setting_save')

            business_setting_object = MessageToDict(request)
            print(business_setting_object)
            business_setting = BusinessSettings(**business_setting_object)
            business_setting.save()

            business_setting = parser_one_object(business_setting)

            response = business_setting_pb2.BusinessSettingResponse(business=business_setting)
            print(response)
            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_business_setting_update')

            business_setting_object = MessageToDict(request)
            business_setting = BusinessSettings.objects.get(id=business_setting_object['id'])


            if business_setting:
                del business_setting_object['id']

            business_setting.update(**business_setting_object)

            business_setting = BusinessSettings.objects.get(id=business_setting.id)

            business_setting = parser_one_object(business_setting)
            response = business_setting_pb2.BusinessSettingResponse(business=business_setting)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '05_business_setting_delete')

            business_setting = BusinessSettings.objects.get(id=request.id)
            business_setting = business_setting.delete()

            response = business_setting_pb2.BusinessSettingEmpty()

            return response

        except BusinessSettings.DoesNotExist as e:
            not_exist_code(context, e)


def start_business_setting_service():
    business_setting_pb2_grpc.add_BusinessSettingServicer_to_server(BusinessSettingService(), grpc_server)
