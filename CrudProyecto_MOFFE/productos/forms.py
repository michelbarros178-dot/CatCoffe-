from django import forms
from .models import Gato, Adopcion  # <-- Asegúrate de importar los 3 modelos aquí

# Formulario para Productos

# Formulario para Gatos
class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = ['nombre', 'raza', 'edad', 'descripcion', 'foto', 'disponible_adopcion']

# Formulario para Adopciones
class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['gato', 'cliente', 'fecha_entrega', 'documento_contrato_url']