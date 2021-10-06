from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, default='')

    def __str__(self):
        return self.name[:20]

    class Meta:
        ordering = ['pk']


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанр')
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.name[:20]

    class Meta:
        ordering = ['pk']


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='title')
    name = models.CharField(max_length=200, verbose_name='Произведение')
    year = models.IntegerField(
        validators=[
            MinValueValidator(1200),
            MaxValueValidator(2100)
        ]
    )

    def __str__(self):
        return self.name[:20]

    class Meta:
        ordering = ['pk']
