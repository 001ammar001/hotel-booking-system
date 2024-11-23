from rest_framework import serializers
from hotel.models import HotelRoom


class HotelRoomSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(read_only=True)
    room_number = serializers.IntegerField(read_only=True)
    number_of_rooms = serializers.IntegerField(
        write_only=True, min_value=1, max_value=200
    )

    class Meta:
        model = HotelRoom
        fields = ["type", "room_number", "number_of_rooms"]