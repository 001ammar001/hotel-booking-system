from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (GetHotelsApiView, AddHotelImages)

router = SimpleRouter()
router.register("hotels", GetHotelsApiView)

urlpatterns = [
    path("hotels/<int:hotel_pk>/images", AddHotelImages.as_view())
] + router.urls
