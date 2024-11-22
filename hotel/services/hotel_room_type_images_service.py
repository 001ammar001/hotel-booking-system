from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

from hotel.serializers import HotelRoomTypeImagesListSerializer
from hotel.models import HotelRoomTypeImage


class TypeImagesService:

    @staticmethod
    def get_typeImages(hotel_pk: int, type_id: int) -> Response:
        query = HotelRoomTypeImage.objects \
            .filter(type__hotel_id=hotel_pk, type_id=type_id)\
            .only("id", "image")

        serializer = HotelRoomTypeImagesListSerializer(query, many=True)
        return Response(serializer.data)

    @staticmethod
    def add_images(type_id: int, files) -> Response:
        images = [
            HotelRoomTypeImage(type_id=type_id, image=file)
            for file in files
        ]

        HotelRoomTypeImage.objects.bulk_create(images)

        return Response({"message": "images has been added sucsessfully"}, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete_images(image_ids: list[int], type_id: int):
        images = TypeImagesService.validate_images_existence(
            image_ids, type_id
        )

        for image_file in images:
            image_file.image.delete(False)

        images.delete()

        return Response({"message": "images deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def validate_images_existence(image_ids: list[int], type_id: int):
        if len(image_ids) != len(set(image_ids)):
            raise serializers.ValidationError({
                "message": "dublicate items has been found"
            })

        images = HotelRoomTypeImage.objects.filter(
            id__in=image_ids, type_id=type_id)

        if len(images) != len(image_ids):
            raise serializers.ValidationError({
                "message": "Some Items Does not exist"
            })

        return images
