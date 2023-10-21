from django.db import models

# Create your models here.


class Partners(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    products = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
