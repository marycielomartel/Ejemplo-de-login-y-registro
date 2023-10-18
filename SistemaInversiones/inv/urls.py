from django.urls import path
from .views import home, contacto, registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
]
