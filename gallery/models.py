from django.db import models


# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='covers/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

