from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from subscription.api.v1.serializers import SubscriptionSerializer
from subscription.models import Subscription
from users.models import User


class SubscriptionAPI(APIView):

    def post(self, request: HttpRequest) -> Response:
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request: HttpRequest, subscription_id: int) -> Response:
        try:
            subscription = Subscription.objects.get(pk=subscription_id)
        except ObjectDoesNotExist:
            return Response({"error": "Subscription not found"}, status=404)

        serializer = SubscriptionSerializer(
            subscription, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request: HttpRequest, subscription_id: int) -> Response:
        try:
            subscription = Subscription.objects.get(pk=subscription_id)
        except ObjectDoesNotExist:
            return Response({"error": "Subscription not found"}, status=404)

        subscription.delete()
        return Response(status=204)


class SubscriptionList(APIView):

    def get(self, request: HttpRequest, email: str) -> Response:
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response(
                {"error": f"User with email {email} not found"}, status=404
            )
        subscriptions = Subscription.objects.filter(user=user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data, status=200)
