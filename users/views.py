import random

from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterValidateSerializer, AuthValidateSerializer, ConfirmCodeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmCode


User = get_user_model()

@api_view(['POST'])
def registration_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']
    phone_number = serializer.validated_data.get('phone_number')
    
    user = User.objects.create_user(
        email=email,
        password=password,
        phone_number=phone_number,  
        is_active=False
    )
    
    code = str(random.randint(100000,999999))
    
    ConfirmCode.objects.create(
        user=user,
        code=code
    )
    
    return Response(
        status=status.HTTP_201_CREATED,
        data={'user_id':user.id,
              'code':code
              }
    )   
    
    #1 create api
@api_view(['POST'])
def authorization_api_view(request):
    #2 get data
    serializer = AuthValidateSerializer(data=request.data)
    
    #3 validation check
    serializer.is_valid(raise_exception=True)
    
    #4 I search by username bacause the password is hashed
    user = authenticate(**serializer.validated_data)
    
    if user is not None:
        
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        
    #5 if the user doesn't exist--> 
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = ConfirmCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    code = serializer.validated_data['code']
    
    try:
        confirm_code = ConfirmCode.objects.get(code=code)
        
    except ConfirmCode.DoesNotExist:
        return Response(
            data={'error': 'Invalid code'},
            status=status.HTTP_400_BAD_REQUEST
        )
    user = confirm_code.user    
    
    user.is_active=True
    user.save()
    
    return Response(
        data={
            'message':'User confirm'
        }
    )
        