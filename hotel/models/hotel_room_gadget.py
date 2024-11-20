from django.db import models
from django.core.validators import MinValueValidator
from .hotel_room_type import Hotel


class HotelRoomGadget(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    price = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0)]
    )
    hotel = models.ForeignKey(
        Hotel, related_name="room_gadgets", on_delete=models.CASCADE
    )
