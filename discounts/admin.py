from django.contrib import admin
from .models import PriceLevel, GroupSale, SubscriptionPlan, UserSubscription

admin.site.register(PriceLevel)
admin.site.register(GroupSale)
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
