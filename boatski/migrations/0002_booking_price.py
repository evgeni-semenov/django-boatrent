# Generated by Django 4.2.1 on 2023-05-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boatski', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]