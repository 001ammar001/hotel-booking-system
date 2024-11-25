from rest_framework import serializers
from hotel.models import HotelBooking
from .hotel_booked_gadget_serializer import HotelBookedGadgetSerializer
from shared.serializers.stop_on_first_error_list_serializer import StopOnFirstErrorListSerializer


class RoomBookingSerializer(serializers.ModelSerializer):
    booked_gadgets = HotelBookedGadgetSerializer(many=True)
    
    class Meta:
        model = HotelBooking
        fields = '__all__'

class AddRoomBookingSerializer(serializers.ModelSerializer):
    gadgets = StopOnFirstErrorListSerializer(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = HotelBooking
        fields = [
            "start_date",
            "end_date",
            "gadgets"
        ]

    def validate_gadets(self,gadgets):
        if len(gadgets) != len(set(gadgets)):
            raise serializers.ValidationError(
                "gadgets should be unique for each booking"
            )

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if (end_date < start_date):
            raise serializers.ValidationError(
                "end date must be after start date"
            )

        return super().validate(attrs)
