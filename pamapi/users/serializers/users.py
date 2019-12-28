from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from pamapi.users.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'email'
        )

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username = data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        self.context['user'] = user
        return data
    def create(self, data):
        token, created = Token.objects.get_or_create(user= self.context['user'])
        return self.context['user'], token.key