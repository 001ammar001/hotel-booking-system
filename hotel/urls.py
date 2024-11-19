from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    GetHotelsApiView,
    HotelImagesViewSet,
    HotelStaffsViewSet,
    HotelStaffsDeleteView,
)

router = SimpleRouter(
    use_regex_path=False
)
router.register("hotels", GetHotelsApiView)
router.register(
    "hotels/<int:hotel_pk>/images",
    HotelImagesViewSet,
    basename="hotel-images"
)

urlpatterns = [
    path("hotels/<int:hotel_pk>/staffs/", HotelStaffsViewSet.as_view(),),
    path(
        "hotels/<int:hotel_pk>/staffs/<int:staff_pk>/",
        HotelStaffsDeleteView.as_view()
    )
] + router.urls
