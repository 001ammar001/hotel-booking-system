from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import (
    Hotel
)
from .serializers import (
    HotelListSerializer
)


class GetHotelsApiView(ReadOnlyModelViewSet):
    serializer_class = HotelListSerializer
    queryset = Hotel.objects.defer("hotel_super_admin").all()
