# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment, Contact
from .serializers import AppointmentSerializer, ContactSerializer


# ----------- APPOINTMENTS --------------
@api_view(['POST'])
def book_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Appointment booked successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_appointments(request):
    appointments = Appointment.objects.all().order_by('-id')
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


# ----------- CONTACT FORM --------------
@api_view(['POST'])
def submit_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Message submitted successfully!"}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def list_contacts(request):
    contacts = Contact.objects.all().order_by('-id')
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)
