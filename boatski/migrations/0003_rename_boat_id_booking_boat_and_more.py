# Generated by Django 4.2.1 on 2023-05-29 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boatski', '0002_booking_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='boat_id',
            new_name='boat',
        ),
        migrations.RenameField(
            model_name='dailyrentalprice',
            old_name='boat_id',
            new_name='boat',
        ),
        migrations.AlterUniqueTogether(
            name='dailyrentalprice',
            unique_together={('date', 'boat')},
        ),
    ]
