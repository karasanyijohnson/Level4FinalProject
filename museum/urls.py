from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
    # path('', home, name='home'),
    # path('museum-details/<int:pk>', museumDetails, name='museum-details'),
    # path('booking-museum/<int:mid>', booking, name='book-museum'),
    # path('listOfBookings', listOfBookings, name='listOfBookings'),
    path('cancel/booking/<int:pk>', cancelBooking, name='cancelBooking'),
    path('', Museums, name='museums'),
    path('museum_lists', MuseumList, name='museum_lists'),
    path('museum-detail/<int:pk>', Museum_Detail, name='museum-detail'),
    path('booking/<int:mid>', booking, name='booking'),
    path('yourBookings', yourBookings, name='yourBookings'),
    path('payment/<int:pk>', payment, name="payment"),
    path('charge/', charge, name="charge"),
    path('success/<str:args>/', successMsg, name="success"),

]
