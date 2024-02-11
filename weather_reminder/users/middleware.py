from django.contrib.auth.middleware import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.http import HttpResponseRedirect

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class JWTAuthenticationMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_cookie = False

        if not hasattr(request, "user"):
            request.user = AnonymousUser()

        access_token = request.COOKIES.get("access_token")
        if access_token is not None:
            try:
                AccessToken(access_token).verify()
            except TokenError:

                refresh_token = request.COOKIES.get("refresh_token")
                try:
                    if refresh_token is None:
                        raise TokenError
                    refresh_token = RefreshToken(refresh_token)
                    refresh_token.verify()
                except TokenError:
                    request.path = settings.LOGIN_URL

                else:
                    new_access_token = refresh_token.access_token
                    set_cookie = True

                try:
                    user, _ = JWTAuthentication().authenticate(request)
                    if user is not None:
                        request.user = user
                except:
                    print('Auth with JWTAuthentication dont pass')
                    request.path = settings.LOGIN_URL

        response = self.get_response(request)
        if set_cookie:
            response.set_cookie(
                key="access_token",
                value=str(new_access_token),
                expires=settings.ACCESS_TOKEN_EXPIRE_TIME,
            )
        return response


# class JWTAuthenticationMiddleware2(MiddlewareMixin):
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#
#         if not hasattr(request, "user"):
#             request.user = AnonymousUser()
#
#         access_token = request.COOKIES.get("access_token")
#         refresh_token = request.COOKIES.get("refresh_token")
#
#         if not access_token and not refresh_token:
#             pass
#
#         elif access_token and refresh_token:
#             refresh_and_access(request,response, refresh_token, access_token)
#
#
#
#
# def  refresh_and_access(request, response, refresh_token, access_token):
#
#     try:
#         AccessToken(access_token).verify()
#     except TokenError:
#         new_access_token = refresh_token.access_token
#         response.set_cookie(
#             key="access_token",
#             value=str(new_access_token),
#             expires=settings.ACCESS_TOKEN_EXPIRE_TIME,
#         )
#
#     user, _ = JWTAuthentication().authenticate(request)  # TRY
#     if user is not None:
#         request.user = user
