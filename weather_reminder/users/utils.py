import functools
from datetime import datetime

from django.conf import settings
from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect

from rest_framework_simplejwt.tokens import(
    AccessToken,
    TokenError,
    RefreshToken,
)


def check_access_token(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        access_token = request.COOKIES.get('access_token')
        try:
            if access_token is None:
                raise TokenError
            AccessToken(access_token).verify()
        except TokenError:

            refresh_token = request.COOKIES.get('refresh_token')
            try:
                if refresh_token is None:
                    raise TokenError
                refresh_token = RefreshToken(refresh_token)
                refresh_token.verify()
            except TokenError:
                return redirect('users:login')

            new_access_token = refresh_token.access_token
            response = JsonResponse({"message": "Access token refresh"})
            response.set_cookie(
                key="access_token",
                value=str(new_access_token),
                httponly=True,
                expires=settings.ACCESS_TOKEN_EXPIRE_TIME
            )
            return response

        return func(request, *args, **kwargs)

    return wrapper
