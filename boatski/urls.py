from django.urls import path
from .views import *

urlpatterns = [
    path('', FrontPageView.as_view()),
    path('bookings/', BookingListView.as_view()),
    path('bookings/<int:pk>', BookingUpdateView.as_view()),
]