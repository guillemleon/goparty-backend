from rest_framework import serializers
from users.models import User, UserCustomer, UserCompany
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name', 'phone', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class UserCustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomer
        fields = ['id', 'email', 'first_name',
                  'last_name', 'phone', 'password', 'accepted_terms']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class UserCompanyRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ['id', 'email', 'company_name',
                  'cif', 'phone', 'password', 'country', 'city', 'address', 'description', 'accepted_terms']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        userProfileObj = None
        try:
            userProfileObj = UserCustomer.objects.get(email=self.user)
        except UserCustomer.DoesNotExist:
            userProfileObj = UserCompany.objects.get(email=self.user)

        data['type'] = userProfileObj.type
        data['is_active'] = userProfileObj.is_active
        return data
