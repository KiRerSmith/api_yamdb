# Generated by Django 2.2.16 on 2021-10-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0027_auto_20211012_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='genre_title', to='reviews.Genre'),
        ),
    ]
