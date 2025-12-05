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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders", verbose_name="Пользователь"
    )
    shift = models.ForeignKey(
        ProgramShift, on_delete=models.CASCADE, related_name="orders", verbose_name="Смена"
    )
    group_sale = models.ForeignKey(
        GroupSale,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        verbose_name="Групповая продажа",
    )

    child_name = models.CharField("Имя ребёнка", max_length=255)
    child_age = models.IntegerField("Возраст ребёнка")

    amount = models.DecimalField("Сумма", max_digits=10, decimal_places=2)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="pending")
    payment_method = models.CharField("Способ оплаты", max_length=50, default="card")

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    paid_at = models.DateTimeField("Дата оплаты", null=True, blank=True)

    def __str__(self):
        return f"Заказ #{self.id} — {self.user.email} — {self.amount} руб."

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
