from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()

class UserBaseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    password = serializers.CharField(write_only=True)


class AuthValidateSerializer(UserBaseSerializer):
    pass


class RegisterValidateSerializer(UserBaseSerializer):
    
    phone_number = serializers.CharField(
        required=False,
     allow_blank=True
     )
     
    def validate_email(self, email):  
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists!')
        return email

class ConfirmCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    