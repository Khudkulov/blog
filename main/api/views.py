from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerializer
from main.models import Contact


class ContactListCreateAPIView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer