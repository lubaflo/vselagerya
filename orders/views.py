from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]  # потом можно ужесточить

    def get_queryset(self):
        return Order.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        # если будет аутентификация, можно подставлять self.request.user
        serializer.save()
