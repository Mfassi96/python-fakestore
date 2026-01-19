from django.shortcuts import render, redirect, get_object_or_404
from . forms import CustomUserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import requests



# Create your views here.

def get_products(request):
    response = requests.get('https://fakestoreapi.com/products/')
    products = response.json()
    return render(request, 'store/products.html', {'products': products})

def view_cart(request):
    
    cart = request.session.get('cart', {})
    
    #logica del carrito
    cart_items = []
    total = 0
    
    for product_id, item in cart.items():
        subtotal = float(item['price']) * item['quantity']
        total += subtotal
        cart_items.append({
            'id': product_id,
            'title': item['title'],
            'price': item['price'],
            'quantity': item['quantity'],
            'image': item['image'],
            'subtotal': subtotal
        })
        
    return render(request, 'store/carrito.html', {
        'cart_items': cart_items,
        'total': total
    })

def add_to_cart(request, product_id):
    """Agrega un producto al carrito en la sesión."""
    # Obtenemos el producto de la API 
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
    product = response.json()
    
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'title': product['title'],
            'price': product['price'],
            'image': product['image'],
            'quantity': 1
        }
    
    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    """Elimina un producto del carrito."""
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')



def formulario_registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('get_products')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                 login(request, user)
                 messages.info(request, f"Has iniciado sesión como {username}.")
                 return redirect('get_products')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
        return render(request, 'store/login.html', {'form': form})