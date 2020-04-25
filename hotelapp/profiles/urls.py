from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.displayprofile,name='profile'),
    path('update',views.updateprofile,name='update'),
    ]

