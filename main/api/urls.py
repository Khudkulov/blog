from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactListCreateAPIView

router = DefaultRouter()
router.register('contact', ContactListCreateAPIView, basename='contact')

app_name = 'contact_api'

urlpatterns = [
    path('', include(router.urls))
]