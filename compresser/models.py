from django.db import models


class Compressor(models.Model):
    image = models.ImageField(upload_to='img/')
