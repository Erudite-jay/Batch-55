from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #generate token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), #to verify token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #generate a new AT with the help of RT


    path('custom-token/',views.login_view)
]