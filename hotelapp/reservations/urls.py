from django.urls import path, include
from . import views
from .views import GeneratePDF

urlpatterns = [
    path('',views.bookroom,name='book'),
    path('<int:hotel_id>',views.storebooking,name='reserve'),
    path('mybooking',views.mybooking,name='mybooking'),
    path('cancelbooking/<int:id>',views.cancelbooking,name='cancelbooking'),
    path('mybookings/<int:id>/pdf', GeneratePDF.as_view(), name='gpdf'),
    ]



