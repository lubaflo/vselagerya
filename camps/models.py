from django.db import models
from users.models import User


class Camp(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="camps",
        verbose_name="Владелец",
    )
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True)
    region = models.CharField("Регион", max_length=255)
    address = models.CharField("Адрес", max_length=255)
    geo_lat = models.FloatField("Широта", null=True, blank=True)
    geo_lng = models.FloatField("Долгота", null=True, blank=True)

    age_from = models.IntegerField("Возраст от", default=6)
    age_to = models.IntegerField("Возраст до", default=17)

    food_description = models.TextField("Питание", blank=True)
    accommodation_description = models.TextField("Проживание", blank=True)

    is_verified = models.BooleanField("Проверен", default=False)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Лагерь"
        verbose_name_plural = "Лагеря"


class CampDocument(models.Model):
    camp = models.ForeignKey(
        Camp,
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="Лагерь",
    )
    name = models.CharField("Название документа", max_length=255)
    file = models.FileField("Файл", upload_to="camp_documents/")
    uploaded_at = models.DateTimeField("Дата загрузки", auto_now_add=True)

    def __str__(self):
        return f"{self.camp.title} — {self.name}"

    class Meta:
        verbose_name = "Документ лагеря"
        verbose_name_plural = "Документы лагерей"


class Program(models.Model):
    camp = models.ForeignKey(
        Camp, on_delete=models.CASCADE, related_name="programs", verbose_name="Лагерь"
    )
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    duration_days = models.IntegerField("Длительность (дни)")
    price = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)
    max_children = models.IntegerField("Максимум детей", default=100)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"


class ProgramShift(models.Model):
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="shifts",
        verbose_name="Программа",
    )
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    seats_total = models.IntegerField("Всего мест")
    seats_taken = models.IntegerField("Занято мест", default=0)

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

    class Meta:
        verbose_name = "Смена"
        verbose_name_plural = "Смены"
