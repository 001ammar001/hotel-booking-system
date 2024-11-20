from rest_framework import serializers
from hotel.models import HotelStaff, Hotel


class HotelStaffListSerializer(serializers.Serializer):
    staff_id = serializers.IntegerField(source="id")
    email = serializers.CharField(read_only=True, source="user.email")

    class Meta:
        fields = ['staff_id', 'email']


class AddNewStaffSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    class Meta:
        fields = ["user_id"]

    def validate_user_id(self, user_id: int):
        if HotelStaff.objects.filter(user_id=user_id, hotel_id=self.context["hotel_id"]).exists():
            raise serializers.ValidationError(
                "this user is already a staff for this hotel"
            )

        if Hotel.objects.filter(hotel_super_admin=user_id).exists():
            raise serializers.ValidationError(
                "this user is already a staff for this hotel"
            )

        return user_id
