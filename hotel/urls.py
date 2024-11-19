from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    GetHotelsApiView,
    HotelImagesListCreateView,
    HotelStaffsViewSet
)

router = SimpleRouter(
    use_regex_path=False
)
router.register("hotels", GetHotelsApiView)
router.register(
    "hotels/<int:hotel_pk>/images",
    HotelImagesListCreateView,
    basename="hotel-images"
)
router.register(
    "hotels/<int:hotel_pk>/staffs",
    HotelStaffsViewSet,
    basename="hotel-staffs"
)

urlpatterns = [

] + router.urls
