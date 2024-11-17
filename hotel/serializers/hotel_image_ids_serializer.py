from rest_framework import serializers
from hotel.models import HotelImage


class HotelImageIdsSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, min_length=1,
    )

    def validate(self, attrs):
        ids = attrs.get("ids")
        hotel_pk = self.context.get("hotel_pk")

        if len(ids) != len(set(ids)):
            raise serializers.ValidationError("dublicate items has been found")

        if HotelImage.objects.filter(id__in=ids, hotel_id=hotel_pk).count() != len(ids):
            raise serializers.ValidationError("Some Items Does not exist")
        
        return ids
