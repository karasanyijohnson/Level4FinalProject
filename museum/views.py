from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import BookingForm, CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
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
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password is incorrect')
        context = {}
        return render(request, 'museum/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    datas = Museum.objects.all()
    context = {'datas': datas}
    return render(request, 'base.html', context)


@login_required(login_url='login')
def museumDetails(request, pk):
    details = Museum.objects.get(id=pk)
    context = {'details': details}
    return render(request, 'museum/museumDetails.html', context)


@login_required(login_url='login')
def booking(request,mid):
    museum = Museum.objects.get(id=mid)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                visitor = request.user
                book = form.save(commit=False)
                book.visitor = visitor
                book.museum = museum
                book.save()
                return redirect('home')
        form = BookingForm()
    else:
        return redirect('login')
    return render(request, 'museum/booking.html', {'form': form})

def listOfBookings(request):
    bookings = Booking.objects.filter(visitor=request.user)

    context = {'bookings':bookings}
    return render(request, 'museum/listOfBookings.html',context)
