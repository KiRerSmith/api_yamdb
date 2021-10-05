from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User():
    ...


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
