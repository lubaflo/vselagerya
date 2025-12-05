from django.db import models
from camps.models import ProgramShift
from users.models import User


class PriceLevel(models.Model):
    shift = models.ForeignKey(
        ProgramShift,
        related_name="price_levels",
        on_delete=models.CASCADE,
        verbose_name="Смена",
    )
    threshold = models.IntegerField("Порог участников")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.shift} — {self.threshold} чел. → {self.price} руб."

    class Meta:
        verbose_name = "Ценовой уровень"
        verbose_name_plural = "Ценовые уровни"


class GroupSale(models.Model):
    shift = models.ForeignKey(
        ProgramShift,
        related_name="group_sales",
        on_delete=models.CASCADE,
        verbose_name="Смена",
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    current_members = models.IntegerField("Текущее количество участников", default=1)
    target_members = models.IntegerField("Целевое количество участников")
    is_closed = models.BooleanField("Закрыта", default=False)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"Групповая продажа ({self.current_members}/{self.target_members})"

    @property
    def progress_percent(self):
        return int(self.current_members / self.target_members * 100)

    class Meta:
        verbose_name = "Групповая продажа"
        verbose_name_plural = "Групповые продажи"


class SubscriptionPlan(models.Model):
    name = models.CharField("Название", max_length=255)
    price_monthly = models.DecimalField("Цена в месяц", max_digits=10, decimal_places=2)
    discount_percent = models.IntegerField("Скидка (%)", default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, verbose_name="Тариф")
    start_date = models.DateField("Дата начала", auto_now_add=True)
    is_active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return f"{self.user.email} — {self.plan.name}"

    class Meta:
        verbose_name = "Подписка пользователя"
        verbose_name_plural = "Подписки пользователей"
