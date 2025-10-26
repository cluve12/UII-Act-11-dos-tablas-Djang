from django import forms
from .models import Sucursal, Empleado

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'ciudad', 'telefono']

class EmpleadoForm(forms.ModelForm):
    # Opciones predefinidas para el puesto
    PUESTOS_CHOICES = [
        ('', 'Selecciona un puesto'),
        ('Gerente', 'Gerente'),
        ('Subgerente', 'Subgerente'),
        ('Cajero', 'Cajero'),
        ('Sandwich Artist', 'Sandwich Artist'),
        ('Atención al Cliente', 'Atención al Cliente'),
        ('Limpieza', 'Limpieza'),
        ('Repartidor', 'Repartidor'),
        ('Ayudante General', 'Ayudante General'),
    ]
    
    puesto = forms.ChoiceField(
        choices=PUESTOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Empleado
        fields = ['nombre', 'puesto', 'telefono', 'salario', 'foto_perfil', 'id_sucursal']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salario', 'step': '0.01'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'id_sucursal': forms.Select(attrs={'class': 'form-control'}),
        }