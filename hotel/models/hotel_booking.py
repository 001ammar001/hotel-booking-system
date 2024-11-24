from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from .hotel_room import HotelRoom
from hotel.validators.start_date_validator import start_date_validator

User = settings.AUTH_USER_MODEL


class HotelBooking(models.Model):
    user = models.ForeignKey(
        User, related_name="bookings", on_delete=models.PROTECT
    )

    room = models.ForeignKey(
        HotelRoom, related_name="bookings", on_delete=models.PROTECT
    )

    start_date = models.DateField(validators=[start_date_validator])
    end_date = models.DateField()

    base_price = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0.0)]
    )