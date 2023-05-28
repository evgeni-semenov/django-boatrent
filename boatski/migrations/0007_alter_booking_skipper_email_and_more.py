# Generated by Django 4.2.1 on 2023-05-28 19:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('boatski', '0006_alter_booking_skipper_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='skipper_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='skipper_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]