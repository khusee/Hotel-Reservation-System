from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='listing-index'),
    path('<int:hotel_id>',views.listing,name='listing'),
    path('search',views.search,name='search')
    ]
