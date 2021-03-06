from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.BigIntegerField()
    email = models.EmailField()
    hire_date =models.DateTimeField(default=now(),blank=True)
    def __str__(self):
        return self.name

