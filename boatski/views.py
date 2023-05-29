from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *
from .forms import *

class FrontPageView(TemplateView):
    template_name = "boatski/base.html"

class BookingListView(ListView):
    model = Booking

class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    success_url = "/bookings"

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    success_url = "/"

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = "/"