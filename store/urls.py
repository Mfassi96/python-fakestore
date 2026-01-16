from django.urls import path
from . import views

urlpatterns = [
    # Cuando la ruta esté vacía, llama a la función get_products de views.py
    path('', views.get_products, name='get_products'),
]