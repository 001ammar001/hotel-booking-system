from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, decorators

from .permissions import (HotelOwnerPermission, HotelStaffPermissoin)
from .models import (Hotel, HotelRoomType, HotelRoomGadget)
from .services import *

from .serializers import (
    HotelListSerializer,
    AddNewStaffSerializer,
    HotelRoomTypeSerializer,
    HotelRoomGadgetSerializer,
    HotelRoomTypeDetailSerializer,
    AddRemoveRoomTypeGadgetsSerializer
)


class GetHotelsApiView(ReadOnlyModelViewSet):
    serializer_class = HotelListSerializer
    queryset = Hotel.objects.defer("hotel_super_admin").all()
    lookup_url_kwarg = "hotel_pk"


class HotelImagesViewSet(APIView):
    def get_permissions(self):
        permissions = []
        if self.request.method != "GET":
            permissions.append(HotelStaffPermissoin | HotelOwnerPermission)

        return [permission() for permission in permissions]

    def get(self, request: Request, hotel_pk: int):
        return HotelImageService.get_hotelImages(hotel_id=hotel_pk)

    def post(self, request: Request, hotel_pk: int):
        files = request.FILES.getlist("images")
        if not files:
            return Response(
                {"message": "you should provide at lease one image"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return HotelImageService.add_images(hotel_pk, files)

    def delete(self, request: Request, hotel_pk: int):
        ids = request.POST.getlist("ids")
        return HotelImageService.delete_images(ids, hotel_pk)


class HotelStaffsViewSet(APIView):
    permission_classes = [HotelOwnerPermission]

    def get(self, request: Request, hotel_pk: int):
        return HotelStaffService.get_hotel_staffs(hotel_id=hotel_pk)

    def post(self, request: Request, hotel_pk: int):
        serializer = AddNewStaffSerializer(
            data=request.data,
            context={"hotel_id": hotel_pk}
        )
        serializer.is_valid(raise_exception=True,)

        return HotelStaffService.addNewStaff(user_id=serializer.data.get("user_id"), hotel_id=hotel_pk)


class HotelStaffsDeleteView(APIView):
    permission_classes = [HotelOwnerPermission]

    def delete(self, request: Request, hotel_pk: int, staff_pk: int):
        return HotelStaffService.removeStaff(hotel_id=hotel_pk, staff_id=staff_pk)


class HotelRoomTypesViewSet(ModelViewSet):
    lookup_url_kwarg = "type_pk"

    def get_permissions(self):
        permissions = []
        if self.request.method != "GET":
            permissions.append(HotelStaffPermissoin | HotelOwnerPermission)
        return [permission() for permission in permissions]

    def get_queryset(self):
        if (self.action == "retrieve"):
            return HotelRoomType.objects.\
                filter(hotel_id=self.kwargs["hotel_pk"])\
                .prefetch_related("gadgets")

        return HotelRoomType.objects.filter(hotel_id=self.kwargs["hotel_pk"])

    def get_serializer_class(self):
        if (self.action == "retrieve"):
            return HotelRoomTypeDetailSerializer
        if (self.action == "gadgets"):
            return AddRemoveRoomTypeGadgetsSerializer
        return HotelRoomTypeSerializer

    def get_serializer_context(self):
        return {"hotel_pk": self.kwargs["hotel_pk"]}

    @decorators.action(methods=["post", "delete"], detail=True, url_name="gadgets", url_path="gadgets")
    def gadgets(self, request: Request, hotel_pk: int, type_pk: int):
        return HotelRoomTypeService.add_or_remove_gadgets(
            gadgets=request.data.get("gadgets"),
            hotel_pk=hotel_pk,
            type_pk=type_pk,
            is_add=self.request.method == "POST"
        )


class HotelRoomGadgetsViewSet(ModelViewSet):
    permission_classes = [HotelOwnerPermission | HotelOwnerPermission]
    serializer_class = HotelRoomGadgetSerializer

    def get_queryset(self):
        return HotelRoomGadget.objects.filter(hotel_id=self.kwargs["hotel_pk"])

    def get_serializer_context(self):
        return {"hotel_pk": self.kwargs["hotel_pk"]}
