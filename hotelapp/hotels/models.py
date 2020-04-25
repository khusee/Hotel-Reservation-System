from django.db import models
from datetime import datetime
from agents.models import Agent
# Create your models here.

# Create your models here.
class Hotel(models.Model):
    agents = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    hotel_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    tv_service = models.BooleanField()
    parking = models.BooleanField()
    attached_bathroom = models.BooleanField()
    air_conditioner = models.BooleanField()
    key_card = models.BooleanField()
    wifi_service = models.BooleanField()
    room_service = models.BooleanField()
    total_rooms = models.IntegerField(default=5)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_two = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_three = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    RoomType = models.CharField(max_length=255)
    capacity = models.IntegerField(default=1)
    TotalRooms = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.RoomType