from rest_framework import serializers
from hotel.models import HotelBooking


class RoomBookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    room = serializers.PrimaryKeyRelatedField(read_only=True)
    base_price = serializers.DecimalField(
        decimal_places=2, max_digits=10, read_only=True
    )

    class Meta:
        model = HotelBooking
        fields = '__all__'

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if (end_date < start_date):
            raise serializers.ValidationError(
                "end date must be after start date"
            )

        return super().validate(attrs)
