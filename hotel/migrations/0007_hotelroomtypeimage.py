# Generated by Django 5.1.3 on 2024-11-22 14:04

import django.db.models.deletion
import hotel.models.hotel_room_type_image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_hotelroomtype_number_of_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoomTypeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=hotel.models.hotel_room_type_image.type_images_directory_path)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hotel.hotelroomtype')),
            ],
        ),
    ]
