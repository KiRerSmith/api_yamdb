# Generated by Django 2.2.16 on 2021-10-08 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20211008_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
