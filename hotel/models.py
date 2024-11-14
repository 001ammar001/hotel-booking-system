from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    location_details = models.CharField(max_length=255)
    hotel_super_admin = models.ForeignKey(User, related_name="owner")


class HotelAdmin(models.Model):
    hotel_id = models.ForeignKey(Hotel, related_name="hotel_adimns")
    user_id = models.ForeignKey(User, related_name="hotels")

    class Meta:
        unique_together = ["hotel_id", "user_id"]