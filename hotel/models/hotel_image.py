from django.db import models
from .hotel import Hotel


def hotel_images_directory_path(instance: 'HotelImage', file_name: str) -> str:
    return f"hotel_{instance.hotel.id}/{file_name}"


class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=hotel_images_directory_path)
