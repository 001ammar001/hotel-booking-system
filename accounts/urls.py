from django.urls import path
from .views import GoogleLogin, GoogleLoginCallback, LoginPage, EmailRegister

app_name = "accounts"

urlpatterns = [
    path("login/", LoginPage.as_view(), name="login"),
    path("auth/register", EmailRegister.as_view(), name="register"),
    path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path(
        "api/v1/auth/google/callback/",
        GoogleLoginCallback.as_view(),
        name="google_login_callback",
    ),
]
