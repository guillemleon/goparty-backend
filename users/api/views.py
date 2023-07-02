from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializer import UserCustomerRegisterSerializer, UserCompanyRegisterSerializer


class RegisterCustomerView(APIView):
    def post(self, request):
        serializer = UserCustomerRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCompanyView(APIView):
    def post(self, request):
        serializer = UserCompanyRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
