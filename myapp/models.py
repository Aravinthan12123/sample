from django.db import models

# Create your models here.

class Forms(models.Model):
    name = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)
    dob = models.DateField(blank=True, null=True)