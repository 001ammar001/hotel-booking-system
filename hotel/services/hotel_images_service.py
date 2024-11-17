from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

from hotel.serializers import HotelImagesListSerializer
from hotel.models import HotelImage


class HotelImageService:

    @staticmethod
    def get_hotelImages(hotel_id: int) -> Response:
        query = HotelImage.objects \
            .filter(hotel_id=hotel_id).only("id", "image")

        serializer = HotelImagesListSerializer(query, many=True)
        return Response(serializer.data)

    @staticmethod
    def add_images(hotel_id: int, files) -> Response:
        images = [
            HotelImage(hotel_id=hotel_id, image=file)
            for file in files
        ]

        HotelImage.objects.bulk_create(images)

        return Response({"message": "images has been added sucsessfully"}, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete_images(image_ids: list[int], hotel_id: int):
        images = HotelImageService.validate_images_existence(image_ids, hotel_id)

        for image_file in images:
            image_file.image.delete(False)
        
        images.delete()

        return Response({"message": "images deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def validate_images_existence(image_ids: list[int], hotel_id: int):
        if len(image_ids) != len(set(image_ids)):
            raise serializers.ValidationError("dublicate items has been found")

        images = HotelImage.objects.filter(id__in=image_ids, hotel_id=hotel_id)

        if len(images) != len(image_ids):
            raise serializers.ValidationError("Some Items Does not exist")

        return images
