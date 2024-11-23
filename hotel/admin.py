from django.contrib import admin

from .models import Hotel, HotelStaff,HotelRoom

admin.site.register(Hotel)
admin.site.register(HotelStaff)
admin.site.register(HotelRoom)