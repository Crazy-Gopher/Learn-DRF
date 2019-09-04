import grpc
import json

from . import user_pb2
from . import user_pb2_grpc

from google.protobuf import json_format
from django.contrib.auth.models import User
from polls.serializers import UserSerializer
from django.db.models import Q

class HealthChecker(user_pb2_grpc.UserServiceServicer):

    def HealthCheck(self, request, context):
        return user_pb2.HealthCheckResponse(msg='Looks Cool!')
    
    def GetUser(self, request, context):
        req = json.loads(json_format.MessageToJson(request)) # Convert Request message into Json/Dictionary
        username = req.get('username','')
        user_id = req.get('user_id',None)
        email = req.get('email','')
        
        response = {'error':'success', 'user':None}
        if not username and not user_id and not email:
            response['error'] = 'Missing_required_field'
            return json_format.Parse(json.dumps(response), user_pb2.GetUserResponse(), ignore_unknown_fields=False)
         
        users = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email) | Q(pk=user_id))
        if not users.exists():
            response['error'] = 'user_does_not_exist'
            return json_format.Parse(json.dumps(response), user_pb2.GetUserResponse(), ignore_unknown_fields=False)
        if len(users)>1:
            response['error'] = 'multiple_users_exists'
            return json_format.Parse(json.dumps(response), user_pb2.GetUserResponse(), ignore_unknown_fields=False)
        else:
            user= users[0]

        minimal_serializer = UserSerializer(user)
        response['user'] = minimal_serializer.data
        return json_format.Parse(json.dumps(response), user_pb2.GetUserResponse(), ignore_unknown_fields=False) # Convert Json/Dictionary into Response message

def serve(server):
    user_pb2_grpc.add_UserServiceServicer_to_server(HealthChecker(), server)
