from django import forms
from django.forms import DateInput
from .models import *


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["boat", "start_date", "end_date", "price", "skipper_name", "skipper_email", "skipper_phone"]
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

    def clean(self): # This method will be called automatically when Django calls the is_valid() form check
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        boat = cleaned_data.get('boat')

        if start_date and end_date:
            overlapping_bookings = Booking.objects.filter(
                boat=boat,
                start_date__lte=end_date, #lte = less or equal to
                end_date__gte=start_date #gte = greater or equal to
            )

            if self.instance:
                overlapping_bookings = overlapping_bookings.exclude(pk=self.instance.pk)

            if overlapping_bookings.exists():
                raise forms.ValidationError("A booking with overlapping dates already exists!")