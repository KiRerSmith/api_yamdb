from django.contrib.auth.models import AbstractUser
from django.db import models

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
    code = models.CharField(max_length=5)

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=["username", "email"],
                                    name="uniq_signup"),
        )
