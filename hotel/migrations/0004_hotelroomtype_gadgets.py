# Generated by Django 5.1.3 on 2024-11-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_hotelroomgadget'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroomtype',
            name='gadgets',
            field=models.ManyToManyField(related_name='gadgets', to='hotel.hotelroomgadget'),
        ),
    ]
