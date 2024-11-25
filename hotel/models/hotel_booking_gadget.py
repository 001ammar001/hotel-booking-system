from django.db import models
from django.core.validators import MinValueValidator

from .hotel_room_gadget import HotelRoomGadget
from .hotel_booking import HotelBooking


class HotelBookingGadget(models.Model):
    booking = models.ForeignKey(
        HotelBooking, related_name="booked_gadgets", on_delete=models.PROTECT
    )

    gadget = models.ForeignKey(
        HotelRoomGadget, on_delete=models.PROTECT
    )

    price = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0.0)]
    )
