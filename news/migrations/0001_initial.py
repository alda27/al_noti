# Generated by Django 3.0.7 on 2020-08-23 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Categoria de la Noticia')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nombre de la Etiqueta')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Etiquetas',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titulo de la Noticia')),
                ('preview_content', models.CharField(max_length=300, verbose_name='Contenido Previo de la Noticia')),
                ('body', models.TextField(verbose_name='Contenido de la Noticia')),
                ('slug', models.SlugField(max_length=300, unique_for_date='publish')),
                ('photo', models.ImageField(upload_to='news/%Y/%m/%d/')),
                ('is_popular', models.BooleanField(default=False)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicación')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('status', models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10, verbose_name='Estado de la Noticia')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_news', to=settings.AUTH_USER_MODEL, verbose_name='Autor de la Noticia')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='news.Category', verbose_name='Categoria de la Noticia')),
                ('tags', models.ManyToManyField(related_name='tag_news', to='news.Tag', verbose_name='Tags de la noticia')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ('-publish',),
            },
        ),
    ]