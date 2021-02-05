from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/instructors/%Y/%m/%d/', blank=True, default='profile/testimonial1.png')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
