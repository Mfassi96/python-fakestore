from django.contrib.auth.forms import UserCreationForm, UserChangeForm,forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

class ShippingForm(forms.Form):
    full_name = forms.CharField(
        label="Nombre Completo",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan Pérez'})
    )
    address = forms.CharField(
        label="Dirección de Entrega",
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle, número, depto...'})
    )
    city = forms.CharField(
        label="Ciudad",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Santa Fe'})
    )
    postal_code = forms.CharField(
        label="Código Postal",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 3000'})
    )
    phone = forms.CharField(
        label="Teléfono de Contacto",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 3420000000'})
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan Pérez'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej. correo@correo.com'})
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí...'})
    )
