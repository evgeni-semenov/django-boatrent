from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', FrontPageView.as_view()),

    path('bookings/', BookingListView.as_view(), name='booking_list'),

    path('bookings/new', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete', BookingDeleteView.as_view(), name='booking_delete'),

    path('bookings/confirm/<int:pk>', BookingConfirmationView.as_view(), name='booking_confirmation'),

    path('login',LoginView.as_view(next_page="/")),
    path('logout', LogoutView.as_view(next_page="/")),
]
