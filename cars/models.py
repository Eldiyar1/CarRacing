from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from multiselectfield import MultiSelectField

from .constants import *


class Car(models.Model):
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name='Марка трансфера')
    model = models.CharField(max_length=50, verbose_name='Модель')
    images = models.ImageField(upload_to="cars", verbose_name='Изображения')
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    year = models.PositiveIntegerField(validators=[MinValueValidator(1970)], verbose_name='Год выпуска')
    category = models.CharField(choices=CAR_CATEGORIES, max_length=50, verbose_name='Категория')
    body_type = models.CharField(choices=BODY_TYPES, max_length=50, verbose_name='Тип кузова')
    transmission = models.CharField(choices=TRANSMISSION_TYPES, max_length=50, verbose_name='Тип коробки передач')
    steering = models.CharField(choices=STEERING_TYPES, max_length=50, verbose_name='Руль')
    drive_type = models.CharField(choices=DRIVE_TYPES, max_length=50, verbose_name='Тип привода')
    fuel_type = models.CharField(choices=FUEL_TYPES, max_length=50, verbose_name='Тип топлива')
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, verbose_name='Цвет')
    passenger = models.CharField(choices=SEATING_CAPACITY, max_length=50, verbose_name='Вместимость пассажиров')
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=50, verbose_name='Состояние автомобиля')
    fuel_consumption = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Расход топлива на 100км')
    amenities = MultiSelectField(choices=AMENITIES_CHOICES, max_length=150, verbose_name="Внутренние удобства")
    safety = MultiSelectField(choices=SAFETY_EQUIPMENT_CHOICES, max_length=255, verbose_name='Система безопасности')
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=25, verbose_name='Валюта')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    created_date = models.DateField(auto_now_add=True)
    video = models.URLField(verbose_name='Видео')
    url = models.URLField(verbose_name='Ссылка')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Слаг")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Авто"
        verbose_name_plural = "Авто"


class CarReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Название трансфера',
                            related_name='reviews')
    comment = models.TextField(max_length=500, blank=True, null=True, verbose_name='Комментарий')
    date_added = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"Отзыв от {self.user} на {self.car}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
