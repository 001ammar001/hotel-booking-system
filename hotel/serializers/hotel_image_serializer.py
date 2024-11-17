from rest_framework import serializers
from hotel.models.hotel_image import HotelImage


class HotelImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        
        fields = [
            'id',
            "image",
        ]
