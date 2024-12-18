from rest_framework import serializers
from hotel.models.hotel import Hotel


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        
        fields = [
            "id",
            "name",
            "city",
            "country",
            "location_details",
        ]
