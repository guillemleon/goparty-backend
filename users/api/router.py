from django.urls import path
from users.api.views import RegisterCustomerView, RegisterCompanyView, LoginView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('auth/register/customer/', RegisterCustomerView.as_view()),
    path('auth/register/company/', RegisterCompanyView.as_view()),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]
