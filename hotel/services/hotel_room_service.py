from django.db.models.aggregates import Max
from rest_framework.response import Response
from rest_framework import status

from hotel.models import HotelRoom, HotelRoomType
from hotel.serializers.hotel_room_serializer import HotelRoomSerializer


class HotelRoomService:
    @staticmethod
    def add_rooms(hotel_pk: int, type_pk: int, data):
        serializer = HotelRoomSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        number_of_rooms = serializer.validated_data.get("number_of_rooms")

        types = HotelRoomType.objects.filter(hotel__id=hotel_pk)\
            .values_list("id", flat=True)

        current_max_room_number = HotelRoom.objects.filter(type_id__in=types).aggregate(
            max_room=Max("room_number", default=0),
        )

        rooms = [
            HotelRoom(type_id=type_pk,
                      room_number=n + current_max_room_number["max_room"]
                      ) for n in range(1, number_of_rooms + 1)
        ]

        HotelRoom.objects.bulk_create(rooms)

        return Response(
            {"message": f"{number_of_rooms} has been added sucsessfully"},
            status=status.HTTP_201_CREATED
        )
