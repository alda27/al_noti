# Generated by Django 3.0.7 on 2020-09-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_user_save'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='preview_content',
            field=models.CharField(max_length=200, verbose_name='Contenido Previo de la Noticia'),
        ),
    ]