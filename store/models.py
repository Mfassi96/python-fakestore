# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    full_name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    postal_code = models.CharField(max_length=20, verbose_name="Código Postal")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    items = models.JSONField(default=list, verbose_name="Items del Pedido")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Pagado")
    payment_status = models.BooleanField(default=False, verbose_name="Estado de Pago")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    def __str__(self):
        return f"Pedido {self.id} - {self.full_name}"

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Mensaje")
    comprobante = models.ImageField(upload_to='comprobantes/', verbose_name="Comprobante de Pago")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Recepción")
    
    def __str__(self):
        return f"Consulta de {self.name} - {self.created_at.strftime('%d/%m/%Y')}"
