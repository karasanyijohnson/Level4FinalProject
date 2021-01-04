from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import BookingForm, CreateUserForm
from django.urls import reverse

import stripe

stripe.api_key = "sk_test_51I5d2DHTspjo0zkr50YBLy5BlsmUhUw0vGTYXtLwH6LiFCV5C14E3DYthlfgOBG1a3eBEKIdx5aUmT1vFOxAxisR003i7niHkF"


def payment(request, pk):
    pay = Booking.objects.get(id=pk)
    context = {'pay': pay}
    return render(request, 'base/payment.html', context)


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description="Booking museum"

        )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'base/success.html', {'amount': amount})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('museum_lists')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
        context = {'form': form}
        return render(request, 'museum/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('museums')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('museum_lists')
            else:
                messages.info(request, 'Username Or Password is incorrect')
        context = {}
        return render(request, 'museum/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def booking(request, mid):
    museum = Museum.objects.get(id=mid)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                visitor = request.user
                checkin = form.cleaned_data.get('check_in')
                checkout = form.cleaned_data.get('check_out')
                case_1 = Booking.objects.filter(museum=museum, visitor=visitor, check_in=checkin,
                                                check_out=checkout).exists()
                if case_1:
                    return render(request, 'Museums/toBook.html',
                                  {'form': form, 'errors': 'This museum can not be booked twice'})
                book = form.save(commit=False)
                book.visitor = visitor
                book.museum = museum
                book.save()
                messages.success(request, 'Make payment before 2days otherwise your booking will be cancelled')
                return redirect('yourBookings')
        form = BookingForm()
    else:
        return redirect('museum_lists')
    return render(request, 'Museums/toBook.html', {'form': form}, )


def cancelBooking(request, pk):
    booking = get_object_or_404(Booking, id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('yourBookings')
    return render(request, 'Museums/cancelYourBooking.html', {'booking': booking})


def Museums(request):
    return render(request, 'Museums/index.html')


@login_required(login_url='login')
def MuseumList(request):
    museums = Museum.objects.all()
    context = {'museums': museums}
    return render(request, 'Museums/Museums.html', context)


@login_required(login_url='login')
def Museum_Detail(request, pk):
    details = Museum.objects.get(id=pk)
    context = {'details': details}
    return render(request, 'Museums/MuseumDetail.html', context)


def yourBookings(request):
    bookings = Booking.objects.filter(visitor=request.user)
    return render(request, 'Museums/yourBookings.html', {'bookings': bookings})
