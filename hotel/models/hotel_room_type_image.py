from django.db import models
from .hotel_room_type import HotelRoomType


def type_images_directory_path(instance: 'HotelRoomTypeImage', file_name: str) -> str:
    return f"hotel_images/hotel_{instance.type.hotel.id}/type_{instance.type.name}/{file_name}"


class HotelRoomTypeImage(models.Model):
    image = models.ImageField(upload_to=type_images_directory_path)
    type = models.ForeignKey(
        HotelRoomType, related_name="images", on_delete=models.CASCADE
    )
