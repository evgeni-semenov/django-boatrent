# Generated by Django 4.2.1 on 2023-05-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boatski', '0004_rename_boat_booking_boat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalprice',
            name='bookings_json',
            field=models.JSONField(null=True),
        ),
    ]