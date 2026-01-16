from django.shortcuts import render
import requests


# Create your views here.

def get_products(request):
    response = requests.get('https://fakestoreapi.com/products/')
    products = response.json()
    return render(request, 'store/products.html', {'products': products})
