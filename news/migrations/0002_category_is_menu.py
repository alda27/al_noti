# Generated by Django 3.0.7 on 2020-08-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_menu',
            field=models.BooleanField(default=False),
        ),
    ]
