from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Boat(models.Model):
    name = models.CharField(max_length = 50)
    reg_number = models.CharField(max_length = 10)
    owner_name = models.CharField(max_length = 100)
    owner_email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class DailyRentalPrice(models.Model):
    date = models.DateField()
    daily_rent = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("date", "boat")
    
    def __str__(self):
        return f"{self.boat}: {self.date}: {self.daily_rent}€"
   

class Booking(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    skipper_name = models.CharField(max_length = 150)
    skipper_email = models.EmailField(blank=True)
    skipper_phone = PhoneNumberField(blank=True)

    def calculate_price(self): # This method calculates the rental price based on daily prices
        total_price = 0
        daily_prices = DailyRentalPrice.objects.filter(
            boat=self.boat, 
            date__range=(self.start_date, self.end_date)
        )

        for daily_price in daily_prices:
            total_price += daily_price.daily_rent
        self.price = total_price
    
    def save(self, *args, **kwargs): # This overrides Django's own save() method and calls calculate_price() to populate the correct price
        self.calculate_price()
        super(Booking, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.boat}: {self.start_date} - {self.end_date}: {self.price}€"