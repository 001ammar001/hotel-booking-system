from django.db import models
from .hotel import Hotel


class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name="types", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ["hotel", "name"]
