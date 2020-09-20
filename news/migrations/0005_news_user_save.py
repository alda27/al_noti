# Generated by Django 3.0.7 on 2020-09-15 22:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_auto_20200825_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='user_save',
            field=models.ManyToManyField(blank=True, related_name='news_saved', to=settings.AUTH_USER_MODEL),
        ),
    ]
