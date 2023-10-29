from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    year_joined = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
