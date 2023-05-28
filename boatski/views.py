from django.views.generic import TemplateView, ListView, UpdateView
from .models import *

class FrontPageView(TemplateView):
    template_name = "boatski/base.html"

class BookingListView(ListView):
    model = Booking

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ["startDate", "endDate", "boat_id", "skipper_name", "skipper_email", "skipper_phone"]
    success_url = "/bookings"