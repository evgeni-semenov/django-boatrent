# from datetime import datetime
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from .models import *
from .forms import *

class FrontPageView(TemplateView):
    template_name = "boatski/frontpage.html"

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    success_url = "/bookings"

class BookingCreateView(CreateView):
    model = Booking
    form_class = CreateBookingForm

    def form_valid(self, form):
        self.object = form.save(commit=False)  # get the uncommitted booking instance
        self.object.price = self.object.calculate_price()  # calculate price before saving
        self.object.save()  # now save booking to the database
        return redirect('booking_confirmation', pk=self.object.pk)  # 'booking_confirmation' should match the name given in urls.py

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = "/"

class BookingConfirmationView(SuccessMessageMixin, DetailView):
    model = Booking
    template_name = "boatski/booking_confirmation.html"
    context_object_name = "booking"
    success_url = "/"
    success_message = "Booking completed. You will be contacted for details!"
