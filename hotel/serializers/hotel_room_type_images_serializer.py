from rest_framework import serializers
from hotel.models import HotelRoomTypeImage


class HotelRoomTypeImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomTypeImage
        
        fields = [
            'id',
            "image",
        ]
