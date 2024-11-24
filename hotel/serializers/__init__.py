from .hotel_list_serializer import HotelListSerializer
from .hotel_image_serializer import HotelImagesListSerializer

from .hotel_staff_serializers import (
    HotelStaffListSerializer,
    AddNewStaffSerializer
)

from .hotel_room_type_serializers import (
    HotelRoomTypeSerializer, HotelRoomTypeDetailSerializer)

from .hotel_room_gadgets_serializers import (
    HotelRoomGadgetSerializer,
    AddRemoveRoomTypeGadgetsSerializer
)

from .hotel_room_type_images_serializer import HotelRoomTypeImagesListSerializer
from .hotel_room_serializer import HotelRoomSerializer
from .hotel_booking_serializers import RoomBookingSerializer