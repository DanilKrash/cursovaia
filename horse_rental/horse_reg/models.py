from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        if not email or not password:
            raise ValueError('Не заданы email или пароль!')
        if 'username' not in kwargs.keys():
            raise ValueError('Не задано имя пользователя!')

        user = CustomUser(email=email, **kwargs)
        user.set_password(password)
        user.save()
        user.is_active = False
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = False

        return self.create_user(email, password, *args, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=128, unique=True, db_index=True, blank=False, verbose_name='Почта')
    is_active = models.BooleanField(blank=False, default=False, verbose_name='Активен')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()


User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    img = models.ImageField(upload_to='users/%Y/%m/%d/', verbose_name='Аватар')
    body = models.TextField(verbose_name='О себе')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, blank=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль пользователя {self.user}'

