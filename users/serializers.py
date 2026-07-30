from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=155)
    password = serializers.CharField()


class AuthValidateSerializer(UserBaseSerializer):
    pass


class RegisterValidateSerializer(UserBaseSerializer):
     
    def validate_username(self, username):  
        try:
            User.objects.get(username=username)
            
        except User.DoesNotExist:
            return username
        
        raise ValidationError('Username already exists!')
    


class ConfirmCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    