from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken

from users.api.v1.serializers import UserSerializer
from users.models import User


class Register(APIView):
    def post(self, request: HttpRequest) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    def post(self, request: HttpRequest) -> Response:
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed(
                f"User with with email {email} not found"
            )
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        refresh_token = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Login successful",
                "refresh": str(refresh_token),
                "access": str(refresh_token.access_token),
            }
        )
