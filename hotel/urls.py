from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    GetHotelsApiView,
    HotelImagesViewSet,
    HotelStaffsViewSet,
    HotelStaffsDeleteView,
    HotelRoomTypesViewSet,
    HotelRoomGadgetsViewSet,
)

router = SimpleRouter(
    use_regex_path=False
)
router.register("hotels", GetHotelsApiView)

router.register(
    "hotels/<int:hotel_pk>/room-types",
    HotelRoomTypesViewSet,
    basename="hotel-room-types"
)

router.register(
    "hotels/<int:hotel_pk>/room-gadgets",
    HotelRoomGadgetsViewSet,
    basename="hotel-room-gadgets"
)

urlpatterns = [
    path("hotels/<int:hotel_pk>/images/",
         HotelImagesViewSet.as_view(),
         ),
    path("hotels/<int:hotel_pk>/staffs/",
         HotelStaffsViewSet.as_view(),
         ),
    path(
        "hotels/<int:hotel_pk>/staffs/<int:staff_pk>/",
        HotelStaffsDeleteView.as_view(),
    ),
] + router.urls
