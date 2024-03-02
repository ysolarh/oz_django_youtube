from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Subscription


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    def validate(self, data):
        print(data)  # dict
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError("You can't subscribe to yourself")
        return data