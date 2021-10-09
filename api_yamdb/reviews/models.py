<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    password = models.CharField(max_length=10, default=None, blank=True)
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
=======
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User():
    ...
>>>>>>> d3737c12f4e6f58f7e54ef10e5bc580632cf75ab


class Category():
    ...


class Genre():
    ...


class Title():
    ...


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
