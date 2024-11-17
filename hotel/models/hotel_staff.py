from django.db import models
from django.conf import settings
from .hotel import Hotel

User = settings.AUTH_USER_MODEL


class HotelStaff(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name="hotel_admins", on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User, related_name="hotels", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["hotel", "user"]
