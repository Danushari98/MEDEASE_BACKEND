# api/urls.py
from django.urls import path
from .views import (
    book_appointment, list_appointments,
    submit_contact, list_contacts
)

urlpatterns = [
    path('appointments/book/', book_appointment),
    path('appointments/', list_appointments),

    path('contact/submit/', submit_contact),
    path('contact/', list_contacts),
]
