from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from hotel.serializers import AddRemoveRoomTypeGadgetsSerializer
from hotel.models import HotelRoomType


class HotelRoomTypeService:

    @staticmethod
    def add_or_remove_gadgets(gadgets: list[int], hotel_pk: int, type_pk: int, is_add: bool):
        data = {"gadgets": gadgets}
        context = {"hotel_pk": hotel_pk, "type_pk": type_pk}
        serializer = AddRemoveRoomTypeGadgetsSerializer(
            data=data, context=context,
        )
        serializer.is_valid(raise_exception=True)
        validated_gadgets = serializer.validated_data.get("gadgets")
        
        hotel_type = get_object_or_404(
            HotelRoomType, id=type_pk, hotel_pk=hotel_pk
        )

        if is_add:
            hotel_type.gadgets.add(*[gadget for gadget in validated_gadgets])
        else:
            hotel_type.gadgets.remove(
                *[gadget for gadget in validated_gadgets])

        return Response({"message": "operations finished sucessfully"})
