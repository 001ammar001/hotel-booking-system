from django.db import transaction
from django.db.models import Q, OuterRef, Exists

from rest_framework.response import Response
from rest_framework import status, serializers

from hotel.models import HotelBooking, HotelRoom, HotelRoomGadget, HotelBookingGadget, HotelRoomType
from hotel.serializers import RoomBookingSerializer, AddRoomBookingSerializer


class HotelBookingService:
    @staticmethod
    def add_booking(data, type_pk: int, user):

        serializer = AddRoomBookingSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        start_date = serializer.validated_data.get("start_date")
        end_date = serializer.validated_data.get("end_date")
        gadgets_ids = serializer.validated_data.get("gadgets")

        gadgets = HotelBookingService.__get_type_gadgets(
            type_pk=type_pk, gadgets_ids=gadgets_ids
        )

        valid_room = HotelBookingService.__get_first_valid_room(
            start_date=start_date,
            end_date=end_date,
            type_pk=type_pk
        )

        booking = HotelBookingService.__perform_booking_creation(
            start_date=start_date,
            end_date=end_date,
            room=valid_room,
            gadgets=gadgets,
            user=user,
        )

        booking_data = HotelBooking.objects.prefetch_related(
            "booked_gadgets__gadget").get(id=booking.id)

        booking_serializer = RoomBookingSerializer(booking_data)

        return Response(booking_serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_hotel_type_bookings(type_pk):
        data = HotelBooking.objects.prefetch_related(
            "booked_gadgets__gadget").filter(room__type_id=type_pk)
        serializer = RoomBookingSerializer(data, many=True)
        return Response(serializer.data)

    @staticmethod
    def __get_type_gadgets(type_pk: int, gadgets_ids: int):
        type_gadgets = HotelRoomType.objects\
            .get(id=type_pk).gadgets\
            .filter(id__in=gadgets_ids)

        if (len(type_gadgets) != len(gadgets_ids)):
            raise serializers.ValidationError(
                {"message": "some gadgets does not exist"}
            )

        return type_gadgets

    @staticmethod
    def __get_first_valid_room(start_date: str, end_date: str, type_pk: int) -> HotelRoom:
        invalid_booking = HotelBooking.objects.filter(~(Q(start_date__gt=end_date) | Q(
            end_date__lt=start_date)), room=OuterRef("pk"))

        valid_room = HotelRoom.objects.filter(~Exists(invalid_booking), type_id=type_pk,)\
            .select_related("type").only("id", "type__base_price").first()

        if (not valid_room):
            raise serializers.ValidationError(
                "no empty room has been have for this type in the provided range"
            )

        return valid_room

    @staticmethod
    def __perform_booking_creation(start_date: str, end_date: str, gadgets, room: HotelRoom, user) \
            -> HotelBooking:

        with transaction.atomic():
            booking = HotelBooking.objects.create(
                user=user,
                start_date=start_date,
                end_date=end_date,
                room_id=room.id,
                base_price=room.type.base_price
            )

            booking_gadgets = [
                HotelBookingGadget(
                    booking=booking,
                    gadget=gadget,
                    price=gadget.price
                ) for gadget in gadgets
            ]

            HotelBookingGadget.objects.bulk_create(booking_gadgets)

        return booking
