from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publicado')


class Tag(models.Model):
    name = models.CharField(max_length=70, verbose_name='Nombre de la Etiqueta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ('-created',)


class Article(models.Model):
    STATUS_CHOICES = (('borrador', 'Borrador'),
                      ('publicado', 'Publicado'),)
    title = models.CharField(max_length=250, verbose_name="Titulo del articulo")
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='slug del articulo')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_articles',
                               verbose_name='Autor del articulo')
    body = models.TextField(verbose_name='Contenido del articulo')
    photo = models.ImageField(upload_to='article/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags_articles', verbose_name='Etiquetas del articulo')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Fecha de publicacion')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrador',
                              verbose_name='Estado del articulo')
    objects = models.Manager()  # the default manager
    published = PublishedManager()  # Our custom manager

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail',
                       args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


class Comment(models.Model):
    STATUS_CHOICES = (('desactivado', 'Desactivado'),
                      ('activado', 'Activado'),)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_comment', verbose_name='Autor del comentario')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments',
                                verbose_name='Articulo al que pertenece')
    body = models.TextField(verbose_name='Contenido del comentario')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='activado',
                              verbose_name='Estado del comentario')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ('-created',)

    def __str__(self):
        return self.body
