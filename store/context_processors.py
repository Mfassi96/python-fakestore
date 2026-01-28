from django.conf import settings

def global_settings(request):
    """Hace que la variable TELEFONO_CONTACTO esté disponible en todos los templates."""
    return {
        'TELEFONO_CONTACTO': getattr(settings, 'TELEFONO_CONTACTO', '')
    }