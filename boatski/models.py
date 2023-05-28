from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Boat(models.Model):
    name = models.CharField(max_length = 50)
    reg_number = models.CharField(max_length = 10)
    owner_name = models.CharField(max_length = 100)
    owner_email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class RentalPrice(models.Model):
    boat_id = models.ForeignKey(Boat, on_delete=models.CASCADE, null=True)
    daily_price = models.PositiveIntegerField(blank=True)
    bookings_json = models.JSONField(null=True)

    def __str__(self):
        return f"{self.boat}: {self.boat.reg_number}"
   

class Booking(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    boat_id = models.ForeignKey(Boat, on_delete=models.CASCADE, null=True)
    skipper_name = models.CharField(max_length = 150)
    skipper_email = models.EmailField(blank=True)
    skipper_phone = PhoneNumberField(blank=True)
    
    def __str__(self):
        return f"{self.boat_id}: {self.startDate} - {self.endDate}"