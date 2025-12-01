from django.db import models
from users.models import User


class Camp(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="camps")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    geo_lat = models.FloatField(null=True, blank=True)
    geo_lng = models.FloatField(null=True, blank=True)

    age_from = models.IntegerField(default=6)
    age_to = models.IntegerField(default=17)

    food_description = models.TextField(blank=True)
    accommodation_description = models.TextField(blank=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CampDocument(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE, related_name="documents")
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="camp_documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.camp.title} — {self.name}"


class Program(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE, related_name="programs")
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_children = models.IntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProgramShift(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="shifts")
    start_date = models.DateField()
    end_date = models.DateField()
    seats_total = models.IntegerField()
    seats_taken = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.program.title} — {self.start_date}"

    @property
    def seats_left(self):
        return self.seats_total - self.seats_taken

    @property
    def fill_percent(self):
        if self.seats_total == 0:
            return 0
        return int(self.seats_taken / self.seats_total * 100)
