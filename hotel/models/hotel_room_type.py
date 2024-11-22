from django.db import models
from django.core.validators import MinValueValidator
from .hotel import Hotel
from .hotel_room_gadget import HotelRoomGadget


class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name="types", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[MinValueValidator(0.0)]
    )

    gadgets = models.ManyToManyField(HotelRoomGadget, related_name="gadgets")

    class Meta:
        unique_together = ["hotel", "name"]
