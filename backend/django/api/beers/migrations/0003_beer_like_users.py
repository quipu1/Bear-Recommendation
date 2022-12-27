# Generated by Django 3.2.1 on 2021-09-30 02:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='like_users',
            field=models.ManyToManyField(related_name='likes_beers', through='beers.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]