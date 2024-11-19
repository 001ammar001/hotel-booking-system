from rest_framework.response import Response

from hotel.models import HotelStaff
from hotel.serializers import HotelStaffListSerializer

class HotelStaffService:

    @staticmethod
    def get_hotel_staffs(hotel_id: int):
        data = HotelStaff.objects.select_related("user").filter(hotel_id=hotel_id).only(
            "user__email", "id")

        serializer = HotelStaffListSerializer(data, many=True)

        return Response(data=serializer.data)
