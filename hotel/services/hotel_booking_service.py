from django.db.models import Q, OuterRef, Exists
from rest_framework.response import Response
from rest_framework import status, serializers

from hotel.serializers import RoomBookingSerializer
from hotel.models import HotelBooking, HotelRoom


class HotelBookingService:
    @staticmethod
    def add_booking(data, type_pk: int, user):

        serializer = RoomBookingSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        start_date = serializer.validated_data.get("start_date")
        end_date = serializer.validated_data.get("end_date")

        invalid_booking = HotelBooking.objects.filter(~(Q(start_date__gt=end_date) | Q(
            end_date__lt=start_date)), room=OuterRef("pk"))

        valid_room = HotelRoom.objects.filter(~Exists(invalid_booking),type_id=type_pk,)\
            .select_related("type").only("id", "type__base_price").first()

        if (not valid_room):
            raise serializers.ValidationError(
                "no empty room has been have for this type in the provided range"
            )

        booking = HotelBooking.objects.create(
            user=user,
            start_date=start_date,
            end_date=end_date,
            room_id=valid_room.id,
            base_price=valid_room.type.base_price
        )

        booking_serializer = RoomBookingSerializer(booking)

        return Response(booking_serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_hotel_type_bookings(type_pk):
        data = HotelBooking.objects.filter(room__type_id=type_pk)
        serializer = RoomBookingSerializer(data, many=True)
        return Response(serializer.data)
