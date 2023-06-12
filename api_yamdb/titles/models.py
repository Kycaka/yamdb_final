from django.db import models

from reviews.models import Title


class Genre(models.Model):
    """Модель жанра."""
    name = models.CharField('Жанр', max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.slug


class Category(models.Model):
    """Модель категории."""
    name = models.CharField('Категория', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug


class Title(Title):
    """Модель произведения."""
    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
