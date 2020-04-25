from django.db import models
from hotels.models import Hotel,Room
from django.contrib.auth.models import User
# Create your models here.

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    person = models.TextField(default=1)
    room = models.TextField(default=1)
    checkin = models.DateField(auto_now=True)
    checkout = models.DateField(auto_now=True)
    totalprice = models.TextField()


