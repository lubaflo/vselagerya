from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Обычный пользователь. Логин — по email.
        """
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)

        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Суперпользователь для админки.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_platform_admin", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    """
    Кастомный пользователь:
    - логин по email
    - простой флаг is_platform_admin
    - обязательные флаги для админки: is_staff, is_superuser, is_active
    """

    email = models.EmailField("Email", unique=True)

    is_platform_admin = models.BooleanField("Админ платформы", default=False)
    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Статус персонала", default=False)
    is_superuser = models.BooleanField("Суперпользователь", default=False)
    date_joined = models.DateTimeField("Дата регистрации", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # при createsuperuser будет спрашивать только email и пароль

    def __str__(self):
        return self.email

    # очень простая модель прав: суперпользователь или админ платформы
    # имеют все права
    def has_perm(self, perm, obj=None):
        return self.is_superuser or self.is_platform_admin

    def has_module_perms(self, app_label):
        return self.is_superuser or self.is_platform_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class ParentProfile(models.Model):
    """
    Профиль родителя, как было раньше.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="parent_profile")

    def __str__(self):
        return f"Parent {self.user.email}"


class Child(models.Model):
    """
    Ребёнок, как было раньше.
    """
    parent = models.ForeignKey(ParentProfile, on_delete=models.CASCADE, related_name="children")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


