# Generated by Django 3.0.7 on 2020-08-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200826_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to='article/%Y/%m/%d/'),
        ),
    ]
