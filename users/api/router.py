from django.urls import path
from users.api.views import RegisterCustomerView, RegisterCompanyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/register/customer/', RegisterCustomerView.as_view()),
    path('auth/register/company/', RegisterCompanyView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
