from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subscription
from .serializers import SubscriptionSerializer


# api/v1/subscriptions
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data
        # json -> object
        serializer = SubscriptionSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# api/v1/subscriptions/{user_id}
class SubscriptionDetail(APIView):
    def delete(self, request, pk):
        subs = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        subs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
