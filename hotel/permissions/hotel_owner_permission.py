from rest_framework.permissions import BasePermission
from hotel.models import Hotel


class HotelOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        hotel_id = view.kwargs.get("hotel_pk")
        try:
            hotel = Hotel.objects.only("hotel_super_admin").get(id=hotel_id)
        except Hotel.DoesNotExist:
            return False
        return hotel and hotel.hotel_super_admin_id == request.user.id