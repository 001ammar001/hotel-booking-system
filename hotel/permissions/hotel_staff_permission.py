from rest_framework.permissions import BasePermission
from hotel.models import HotelStaff


class HotelStaffPermissoin(BasePermission):
    def has_permission(self, request, view):
        hotel_id = view.kwargs.get("hotel_pk")

        return HotelStaff.objects.filter(
            hotel_id=hotel_id, user_id=request.user.id
        ).exists()
