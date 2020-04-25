from django.shortcuts import render, redirect, reverse
import datetime
from hotels.models import Hotel,Room
from .models import Reservation
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .utils import render_to_pdf

from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
class GeneratePDF(View):
    def get(self,request, *args, **kwargs):
        booking = Reservation.objects.get(id= self.kwargs['id'])
        template = get_template('invoice.html')
        context = {"booking":booking}
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

def bookroom(request,hotel_id,room_id):
    if request.mothod == 'GET':
        FirstDate = request.POST['checkin']
        SecDate = request.POST['checkout']

        Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
        Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
        timedeltaSum = Checkout - Checkin
        StayDuration = timedeltaSum.days

        Hotels = Hotel.objects.get(id=hotel_id)

        price = Hotel.Price
        TotalCost = StayDuration * price

        context = {
            'price': price,
            'duration': StayDuration,
            'totalcost': TotalCost
        }

        return render(request,'reservations/reservation.html',context=context)
    else:
        return None


def storebooking(request,hotel_id):
    if request.method == 'GET':
        user = request.user
        FirstDate = request.GET['checkin']
        SecDate = request.GET['checkout']
        person = request.GET['person']
        room = request.GET['room']
        Checkin = datetime.datetime.strptime(FirstDate, "%Y-%m-%d").date()
        Checkout = datetime.datetime.strptime(SecDate, "%Y-%m-%d").date()
        timedeltaSum = Checkout - Checkin
        StayDuration = timedeltaSum.days
        print(StayDuration)
        hotel = get_object_or_404(Hotel,pk=hotel_id)
        price = hotel.price
        TotalCost = StayDuration * price
        cost = TotalCost
        print(person,TotalCost)
        Reservations = Reservation.objects.create(hotel = hotel,user = user, person=person, room=room, checkin = FirstDate, checkout = SecDate, totalprice=TotalCost)
        Reservations.save()
        context = {
            'reservations':Reservations
        }
    return redirect('profile')

def cancelbooking(request,id):
    booking = Reservation.objects.get(id = id)
    booking.delete()
    currentuser = request.user
    return redirect('profile')

def mybooking(request):
    bookings = Reservation.objects.filter(user = request.user)
    context = {
        'bookings':bookings
    }
    return render(request,'reservations/list.html',context=context)

