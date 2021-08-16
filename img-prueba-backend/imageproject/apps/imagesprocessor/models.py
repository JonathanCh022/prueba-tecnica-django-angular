from django.db import models


class Imagen(models.Model):
    file = models.ImageField(upload_to='imagen',blank=False, null=False)

