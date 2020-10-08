from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')


class Tag(models.Model):
    name = models.CharField(max_length=70, verbose_name='Nombre de la Etiqueta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ('-created',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Categoria de la Noticia', unique=True)
    is_menu = models.BooleanField(default=False, verbose_name='Categoria en el menu')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:news_list', args=[self.name, self.id])


class News(models.Model):
    STATUS_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=300, verbose_name='Titulo de la Noticia')
    preview_content = models.CharField(max_length=100, verbose_name='Contenido Previo de la Noticia')
    body = RichTextField(verbose_name='Contenido de la Noticia')
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_news',
                               verbose_name='Autor de la Noticia')
    tags = models.ManyToManyField(Tag, related_name='tag_news', verbose_name='Tags de la noticia')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 verbose_name='Categoria de la Noticia')  # TODO: add related name
    photo = models.ImageField(upload_to='news/%Y/%m/%d/')
    is_popular = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Publicación')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrador',
                              verbose_name='Estado de la Noticia')
    user_save = models.ManyToManyField(User, related_name='news_saved', blank=True)
    objects = models.Manager()  # the default manager
    published = PublishedManager()  # Our custom manager

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail',
                       args=[self.category, self.publish.year, self.publish.month, self.publish.day, self.slug])
