from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate  # <--- SE AGREGÓ 'authenticate' AQUÍ
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
import requests

# --- Vistas de Autenticación ---

def formulario_registro(request):
    """Maneja el registro de nuevos usuarios."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "¡Registro exitoso! Bienvenido a la tienda.")
            return redirect('get_products')
        else:
            messages.error(request, "Hubo un error en el registro. Por favor, revisa los datos.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    """Maneja el inicio de sesión."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # 'authenticate' verifica que el usuario y contraseña coincidan
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                return redirect('get_products')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Datos de formulario inválidos.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    """Cierra la sesión del usuario."""
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('get_products')

# --- Vistas de la Tienda ---

def get_products(request):
    """Lista de productos desde la API."""
    response = requests.get('https://fakestoreapi.com/products/')
    products = response.json()
    return render(request, 'store/products.html', {'products': products})

def view_cart(request):
    """Visualización del carrito de compras."""
    cart = request.session.get('cart', {})
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
    """Añade un producto al carrito en la sesión."""
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
    product = response.json()
    
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    
    if p_id in cart:
        cart[p_id]['quantity'] += 1
    else:
        cart[p_id] = {
            'title': product['title'],
            'price': product['price'],
            'image': product['image'],
            'quantity': 1
        }
    
    request.session['cart'] = cart
    request.session.modified = True 
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    """Quita un producto del carrito."""
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart:
        del cart[p_id]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('view_cart')