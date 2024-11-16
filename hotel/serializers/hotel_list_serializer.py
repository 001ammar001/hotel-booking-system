from rest_framework import serializers
from hotel.models_classes.hotel import Hotel


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        
        fields = [
            "name",
            "city",
            "country",
            "location_details",
        ]
