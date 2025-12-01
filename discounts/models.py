from django.db import models
from camps.models import ProgramShift
from users.models import User


class PriceLevel(models.Model):
    shift = models.ForeignKey(ProgramShift, related_name="price_levels", on_delete=models.CASCADE)
    threshold = models.IntegerField()  # сколько участников нужно набрать
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена при достижении уровня

    def __str__(self):
        return f"{self.shift} — {self.threshold} чел. → {self.price} руб."


class GroupSale(models.Model):
    shift = models.ForeignKey(ProgramShift, related_name="group_sales", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    current_members = models.IntegerField(default=1)
    target_members = models.IntegerField()  # нужно участников для скидки
    is_closed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Групповая продажа ({self.current_members}/{self.target_members})"

    @property
    def progress_percent(self):
        return int(self.current_members / self.target_members * 100)


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.IntegerField(default=10)  # скидка на программы

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.email} — {self.plan.name}"
