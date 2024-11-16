from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    location_details = models.CharField(max_length=255)

    hotel_super_admin = models.ForeignKey(
        User, related_name="owner", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
