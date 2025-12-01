from django.db import models
from users.models import User
from camps.models import ProgramShift
from discounts.models import GroupSale


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Ожидает оплаты"),
        ("paid", "Оплачен"),
        ("cancelled", "Отменён"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    shift = models.ForeignKey(ProgramShift, on_delete=models.CASCADE, related_name="orders")
    group_sale = models.ForeignKey(
        GroupSale, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders"
    )

    child_name = models.CharField(max_length=255)
    child_age = models.IntegerField()

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    payment_method = models.CharField(max_length=50, default="card")

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Заказ #{self.id} — {self.user.email} — {self.amount} руб."
