from django.urls import path
from .  import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('', views.Users.as_view()), #api/v1/users
    path('myinfo', views.MyInfo.as_view()), #api/v1/users/myinfo
    path('getToken', obtain_auth_token),

    # Authentication
    path('getToken', obtain_auth_token), #DRF token
    path('login', views.Login.as_view()), # Django Session Login
    path('logout', views.Logout.as_view()), # Django Session Logout
    
    # JWT authentication
    path('login/jwt', views.JWTLogin.as_view()),
    path('login/jwt/info', views.UserDetailView.as_view()),

    # Simple JWT Authentication
    path('login/simpleJWT', TokenObtainPairView.as_view()),
    path('login/simpleJWT/refresh', TokenRefreshView.as_view()),
    path('login/simpleJWT/verify', TokenVerifyView.as_view())


]