#Django REST
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#Serializers
from pamapi.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer
)


class UserLoginAPIView(APIView):
    "User login API View"
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data={
            'user' : UserModelSerializer(user).data,
            'access_token' : token
        }

        return Response(data, status=status.HTTP_201_CREATED)