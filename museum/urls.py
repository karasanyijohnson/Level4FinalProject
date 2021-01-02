from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
    path('', home, name='home'),
    path('museum-details/<int:pk>', museumDetails, name='museum-details'),
    path('booking-museum/<int:mid>', booking, name='book-museum'),
    path('listOfBookings', listOfBookings, name='listOfBookings')
]
