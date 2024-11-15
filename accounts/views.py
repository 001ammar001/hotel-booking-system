import requests
from urllib.parse import urljoin

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class GoogleLoginCallback(APIView):
    def get(self, request):
        code = request.GET.get("code")

        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        token_endpoint_url = urljoin(
            "http://localhost:8000", reverse("accounts:google_login")
        )


        response = requests.post(url=token_endpoint_url, data={"code": code})

        return Response(response.json(), status=status.HTTP_200_OK)


class LoginPage(View):
    def get(self, request):
        return render(
            request,
            "pages/login.html",
            {
                "google_callback_uri": settings.GOOGLE_OAUTH_CALLBACK_URL,
                "google_client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            },
        )
