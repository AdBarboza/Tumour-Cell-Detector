from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import controller

urlpatterns = [
    url(r'',controller.hola, name='hello')
    
]
