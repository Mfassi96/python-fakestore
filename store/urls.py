from django.urls import path
from . import views

urlpatterns = [
    # Cuando la ruta esté vacía, llama a la función get_products de views.py
    path('', views.get_products, name='get_products'),
     path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]