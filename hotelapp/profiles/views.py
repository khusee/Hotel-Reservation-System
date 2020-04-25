from django.shortcuts import render, redirect
from .models import Profile
from reservations.models import Reservation

from django.contrib.auth.models import User

# Create your views here.
def displayprofile(request):
    user = request.user
    bookings = Reservation.objects.filter(user=request.user)

    context = {
        'user':user,
        'bookings':bookings
    }
    return render(request,'profiles/profile.html',context=context)

def displayeditpage(request,profile_id):
    profile = Profile.objects.get(pk=profile_id)
    return render(request,'profiles/profileupdate.html')

def updateprofile(request):
    user = request.user
    context = {
        'user':user
    }
    if request.method =='POST':
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.profile.address = request.POST['address']
        user.profile.phone = request.POST['phonenumber']
        if 'profile-image' in request.FILES:
            doc = request.FILES
            user.profile.image = doc['profile-image']
        user.profile.save()
        return render(request, 'profiles/profile.html', context=context)
    return render(request,'profiles/profileupdate.html',context=context)