from rest_framework import serializers
from .models import PriceLevel, GroupSale, SubscriptionPlan, UserSubscription


class PriceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceLevel
        fields = "__all__"


class GroupSaleSerializer(serializers.ModelSerializer):
    progress_percent = serializers.ReadOnlyField()

    class Meta:
        model = GroupSale
        fields = "__all__"


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = "__all__"
