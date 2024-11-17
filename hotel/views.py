from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated,OR
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .permissions import (HotelOwnerPermission, Ho)

from .models import (
    Hotel,
    HotelImage
)

from .serializers import (
    HotelListSerializer,
    HotelImagesListSerializer
)


class GetHotelsApiView(ReadOnlyModelViewSet):
    serializer_class = HotelListSerializer
    queryset = Hotel.objects.defer("hotel_super_admin").all()
    lookup_url_kwarg = "hotel_pk"


class AddHotelImages(APIView):
    permission_classes = [IsAuthenticated, OR(HotelOwnerPermission,)]
    allowed_methods = ["GET"]

    def get(self, request: Request, hotel_pk: int):
        query = HotelImage.objects \
            .filter(hotel_id=hotel_pk)\
            .only("id", "image")

        serializer = HotelImagesListSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request: Request, hotel_pk: int):
        files = request.FILES.getlist("images")
        if not files:
            return Response({"message": "you should provide at lease one image"}, status=status.HTTP_400_BAD_REQUEST)

        images = [
            HotelImage(hotel_id=hotel_pk, image=file)
            for file in files
        ]

        HotelImage.objects.bulk_create(images)

        return Response({"message": "images has been added sucsessfully"}, status=status.HTTP_201_CREATED)
