from rest_framework import serializers
from hotel.models import HotelRoomGadget


class HotelRoomGadgetSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = HotelRoomGadget
        fields = '__all__'

    def save(self, **kwargs):
        return super().save(hotel_id=self.context["hotel_pk"])
