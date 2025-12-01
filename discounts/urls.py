from django.urls import path
from .views import (
    PriceLevelListView,
    GroupSaleListView,
    SubscriptionPlanListView,
    UserSubscriptionListView
)

urlpatterns = [
    path("price-levels/", PriceLevelListView.as_view()),
    path("group-sales/", GroupSaleListView.as_view()),
    path("subscription-plans/", SubscriptionPlanListView.as_view()),
    path("user-subscriptions/", UserSubscriptionListView.as_view()),
]
