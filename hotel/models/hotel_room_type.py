from django.db import models
from .hotel import Hotel
from .hotel_room_gadget import HotelRoomGadget


class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name="types", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    gadgets = models.ManyToManyField(HotelRoomGadget,related_name="gadgets")

    class Meta:
        unique_together = ["hotel", "name"]
