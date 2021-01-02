from django.contrib import admin
from .models import *




class MuseumAdmin(admin.ModelAdmin):
    list_display = ['category','title','description','price','location']
    list_filter = ['category','location']
    list_per_page = 10


class BookingAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName','email','phoneNumber','museum','visitor','check_in','check_out']
    list_filter = ['check_in','check_out','visitor']
    list_per_page = 10




admin.site.register(Museum,MuseumAdmin)
admin.site.register(Booking,BookingAdmin)

