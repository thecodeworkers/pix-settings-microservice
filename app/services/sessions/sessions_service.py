from google.protobuf.json_format import MessageToDict
from mongoengine.queryset import NotUniqueError
from ...protos import session_pb2, session_pb2_grpc
from ...utils import parser_all_object, parser_one_object, not_exist_code, exist_code, paginate, parser_context
from ...utils.validate_session import is_auth
from ..bootstrap import grpc_server
from ...models import Sessions


class SessionService(session_pb2_grpc.SessionServicer):
    def table(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '100_session_table')

            sessions = Sessions.objects

            response = paginate(sessions, request.page, request.per_page)

            response = session_pb2.SessionTableResponse(**response)

            return response

        except Exception as error:
            raise Exception(error)

    def get_all(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '100_session_get_all')

            sessions = parser_all_object(Sessions.objects.all())

            for session in sessions:
                del session['user']

            response = session_pb2.SessionMultipleResponse(session=sessions)
        except Exception as error:
            raise Exception(error)

        return response

    def get(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '100_session_get')

            session_object = MessageToDict(request)

            session = Sessions.objects.get(userAgent=session_object['userAgent'], ip=session_object['ip'], user=user)
            session = parser_one_object(session)

            del session['user']
            response = session_pb2.SessionResponse(session=session)

            return response

        except Sessions.DoesNotExist as e:
            not_exist_code(context, e)

    def save(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            user = is_auth(auth_token, '100_session_save')

            session_object = MessageToDict(request)

            old_session = Sessions.objects(userAgent=session_object['userAgent'], ip=session_object['ip'], user=user)

            if old_session:
                session_object['id'] = old_session[0].id
                session_object['valid'] = old_session[0].valid
            
            session_object['user'] = user

            session = Sessions(**session_object)
            session.save()

            session = parser_one_object(session)
            del session['user']
            response = session_pb2.SessionResponse(session=session)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def update(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '100_session_update')

            session_object = MessageToDict(request)
            session = Sessions.objects.get(id=session_object['id'])

            if session:
                del session_object['id']

            session.update(**session_object)

            session = Sessions.objects.get(id=session.id)

            session = parser_one_object(session)
            
            del session['user']
            
            response = session_pb2.SessionResponse(session=session)

            return response

        except NotUniqueError as e:
            exist_code(context, e)

    def delete(self, request, context):
        try:
            auth_token = parser_context(context, 'auth_token')
            is_auth(auth_token, '100_session_delete')

            session = Sessions.objects.get(id=request.id)
            session = session.delete()

            response = session_pb2.SessionEmpty()

            return response

        except Sessions.DoesNotExist as e:
            not_exist_code(context, e)


def start_session_service():
    session_pb2_grpc.add_SessionServicer_to_server(SessionService(), grpc_server)
