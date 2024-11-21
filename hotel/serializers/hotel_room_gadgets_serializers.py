from rest_framework import serializers
from coustom.serializers.stop_on_first_error_list_serializer import StopOnFirstErrorListSerializer
from hotel.models import HotelRoomGadget, HotelRoomType


class HotelRoomGadgetSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = HotelRoomGadget
        fields = '__all__'

    def save(self, **kwargs):
        return super().save(hotel_id=self.context["hotel_pk"])


class AddRemoveRoomTypeGadgetsSerializer(serializers.Serializer):
    gadgets = StopOnFirstErrorListSerializer(
        child=serializers.IntegerField(),
        min_length=1
    )

    def to_representation(self, instance):
        return super().to_representation(instance)

    def validate_gadgets(self, gadgets):
        existing_gadgets = HotelRoomGadget.objects.filter(
            hotel_id=self.context.get("hotel_pk"),
            id__in=gadgets
        )

        if len(existing_gadgets) != len(gadgets):
            raise serializers.ValidationError("some items does not exist")

        return existing_gadgets
