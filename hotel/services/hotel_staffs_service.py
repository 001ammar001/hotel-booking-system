from rest_framework.response import Response
from rest_framework import status
from hotel.models import HotelStaff
from hotel.serializers import HotelStaffListSerializer


class HotelStaffService:

    @staticmethod
    def get_hotel_staffs(hotel_id: int):
        data = HotelStaff.objects.select_related("user").filter(hotel_id=hotel_id).only(
            "user__email", "id")

        serializer = HotelStaffListSerializer(data, many=True)

        return Response(data=serializer.data)

    @staticmethod
    def addNewStaff(hotel_id: int, user_id: int):
        data = HotelStaff.objects.create(user_id=user_id, hotel_id=hotel_id)
        serializer = HotelStaffListSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
