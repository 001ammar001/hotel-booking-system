from rest_framework import serializers
from hotel.models import HotelRoomType
from .hotel_room_gadgets_serializers import HotelRoomGadgetSerializer


class HotelRoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomType
        fields = ['id', 'name']

    def validate_name(self, name):
        if HotelRoomType.objects \
            .filter(hotel_id=self.context.get("hotel_pk"), name=name)\
                .exists():
            raise serializers.ValidationError({
                "message": "this type name is already defined"
            })

        return name

    def save(self, **kwargs):
        return super().save(hotel_id=self.context.get("hotel_pk"))


class HotelRoomTypeDetailSerializer(serializers.ModelSerializer):
    gadgets = HotelRoomGadgetSerializer(many=True)
    class Meta:
        model = HotelRoomType
        fields = ['id', 'name','gadgets']