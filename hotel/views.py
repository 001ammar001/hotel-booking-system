from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    HotelListSerializer, HotelImagesListSerializer, HotelImageIdsSerializer
)
from .permissions import (HotelOwnerPermission, HotelStaffPermisson)
from .models import (Hotel, HotelImage)


class GetHotelsApiView(ReadOnlyModelViewSet):
    serializer_class = HotelListSerializer
    queryset = Hotel.objects.defer("hotel_super_admin").all()
    lookup_url_kwarg = "hotel_pk"


class HotelImagesListCreateView(APIView):
    permission_classes = [
        IsAuthenticated,
        HotelStaffPermisson | HotelOwnerPermission
    ]

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

    def delete(self, request: Request, hotel_pk: int):
        ids = request.POST.getlist("ids")
        validated_ids = HotelImageIdsSerializer(
            data={"ids": ids}, context={"hotel_pk": hotel_pk},
        )
        validated_ids.is_valid(raise_exception=True)
        HotelImage.objects.filter(id__in=ids).delete()

        return Response({"message": "image deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
