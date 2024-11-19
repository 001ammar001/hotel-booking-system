from rest_framework import serializers


class HotelStaffListSerializer(serializers.Serializer):
    staff_id = serializers.IntegerField(source="id")
    email = serializers.CharField(read_only=True, source="user.email")

    class Meta:
        fields = ['staff_id', 'email']
