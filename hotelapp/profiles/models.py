from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile-pics',null=True,blank=True, default='background.jpeg')
    phone = models.BigIntegerField(null=True,blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateField(default=datetime.now())

    def __str__(self):
        return f'{self.user} Profile'

@receiver(post_save,sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


