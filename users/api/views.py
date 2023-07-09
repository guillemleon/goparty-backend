from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializer import (
    UserCustomerRegisterSerializer,
    UserCompanyRegisterSerializer,
    MyTokenObtainPairSerializer
)
from users.models import UserCustomer, UserCompany
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterCustomerView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserCustomerRegisterSerializer(data=request.data)
        email = request.data.get('email')
        user_exists = UserCustomer.objects.filter(email=email).exists()

        if user_exists:
            return Response(status=status.HTTP_409_CONFLICT, headers={'message': 'User already registered'})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCompanyView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserCompanyRegisterSerializer(data=request.data)
        email = request.data.get('email')
        user_exists = UserCompany.objects.filter(email=email).exists()

        if user_exists:
            return Response(status=status.HTTP_409_CONFLICT, headers={'message': 'User already registered'})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer
