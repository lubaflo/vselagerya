from rest_framework import generics
from .models import PriceLevel, GroupSale, SubscriptionPlan, UserSubscription
from .serializers import (
    PriceLevelSerializer,
    GroupSaleSerializer,
    SubscriptionPlanSerializer,
    UserSubscriptionSerializer,
)


class PriceLevelListView(generics.ListAPIView):
    queryset = PriceLevel.objects.all()
    serializer_class = PriceLevelSerializer


class GroupSaleListView(generics.ListAPIView):
    queryset = GroupSale.objects.all()
    serializer_class = GroupSaleSerializer


class SubscriptionPlanListView(generics.ListAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer


class UserSubscriptionListView(generics.ListAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
