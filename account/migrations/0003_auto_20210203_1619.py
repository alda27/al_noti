# Generated by Django 3.0.7 on 2021-02-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201013_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profile/testimonial1.png', upload_to='profiles/instructors/%Y/%m/%d/'),
        ),
    ]
