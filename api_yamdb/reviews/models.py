from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    username = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=150)
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        max_length=254)
    bio = models.CharField(
        'Биография',
        blank=True,
        max_length=300,
    )
    role = models.CharField(max_length=15, choices=CHOICES, default='user')
    code = models.CharField(max_length=5, blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=["username", "email"],
                                    name="uniq_signup"),
        )


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name[:20]

    class Meta:
        ordering = ['pk']


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name[:20]

    class Meta:
        ordering = ['pk']


class Title(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='title'
    )
    name = models.CharField(max_length=256, verbose_name='Произведение')
    year = models.IntegerField(
        validators=[
            MinValueValidator(1200),
            MaxValueValidator(2100)
        ]
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание'
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='genre_title'
    )

    def __str__(self):
        return self.name[:20]

    class Meta:
        ordering = ['pk']


class GenreTitle(models.Model):
    title_id = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='title_id'
    )
    genre_id = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='genre_id'
    )


class Review(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='review')
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='review')
    text = models.TextField()
    score = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comment')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comment')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
