from rest_framework import serializers
from hotel.models import HotelBookingGadget
from .hotel_room_gadgets_serializers import HotelRoomGadgetSerializer


class HotelBookedGadgetSerializer(serializers.ModelSerializer):
    gadget = HotelRoomGadgetSerializer()
    class Meta:
        model = HotelBookingGadget
        fields = ["id","price","gadget"]
