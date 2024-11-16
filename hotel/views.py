from rest_framework.generics import ListAPIView

from .models_classes import (
    Hotel
)
from .serializers import (
    HotelListSerializer
)


class GetHotelsApiView(ListAPIView):
    serializer_class = HotelListSerializer
    queryset = Hotel.objects.defer("hotel_super_admin").all()
