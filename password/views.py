from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from .models import Password
from .serializers import PasswordSerializer

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": 'invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    try:
        user = User(
            username=request.data['username'],
            email=request.data['email']
        )
        user.set_password(request.data['password'])
        user.save()
        return Response({"signup":"ok"}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
def list_pass(request):
    try:
        user = request.user
        passwords = user.passwords.all()
        serializer = PasswordSerializer(passwords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
def new_pass(request):
    try:
        user = request.user
        password = Password(
            host=request.data['host'],
            username=request.data['username'],
            email=request.data['email'],
            passwrd=request.data['password'],
            user=user
        )
        password.save()
        serializer = PasswordSerializer(password)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['GET'])
def get_pass(request, id):
    try:
        user = request.user
        password = user.passwords.get(id=id)
        serializer = PasswordSerializer(password)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['DELETE'])
def delete_pass(request, id):
    try:
        user = request.user
        password = user.passwords.get(id=id)
        password.delete()
        serializer = PasswordSerializer(password)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['PUT'])
def edit_pass(request, id):
    try:
        user = request.user
        password = user.passwords.get(id=id)
        password.host = request.data['host']
        password.username = request.data['username']
        password.email = request.data['email']
        password.passwrd = request.data['password']
        password.save()
        serializer = PasswordSerializer(password)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
