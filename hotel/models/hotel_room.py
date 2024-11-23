from django.db import models
from .hotel_room_type import HotelRoomType


class HotelRoom(models.Model):
    type = models.ForeignKey(
        HotelRoomType, related_name="rooms", on_delete=models.CASCADE
    )
    room_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ["type", "room_number"]
