from reviews.models import Category, Comment, Genre, Review, Title, User
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Review
