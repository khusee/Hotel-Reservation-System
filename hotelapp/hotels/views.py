from django.shortcuts import render
from .models import Hotel, Room
from django.shortcuts import get_object_or_404
from reservations.models import Reservation
# Create your views here.
def index(request):
    listings = Hotel.objects.order_by('-list_date').filter(is_published= True)
    for hotel in listings:
        RoomsBooked = Reservation.objects.filter(hotel=hotel)
        count = RoomsBooked.count()
        count = int(count)
        Roomsavailable = hotel.total_rooms
        Roomsavailable = int(Roomsavailable)

        Roomsleft = Roomsavailable - count
        hotel.total_rooms = Roomsleft
    context = {
        'listings': listings
    }
    return render(request,'listings/listings.html',context=context)

def listing(request,hotel_id):
    listing = get_object_or_404(Hotel,pk=hotel_id)
    values = request.GET
    context = {
        'listing': listing,
        'values': values
    }
    return render(request,'listings/detail.html', context=context)

def search(request):
    query_list = Hotel.objects.order_by('-list_date')
    values = request.GET
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            query_list = query_list.filter(city__icontains = location)

    if 'room' in request.GET:
        room = request.GET['room']
        if room:
            query_list = query_list.filter(total_rooms__gte = room)

    context = {
        'query_list' : query_list,
        'values':values
    }

    return render(request, 'listings/search.html', context=context)


