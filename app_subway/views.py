from django.shortcuts import render, get_object_or_404, redirect
from .models import Sucursal, Empleado
from .forms import SucursalForm, EmpleadoForm

# Vistas para Sucursales (Principal)
def listar_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'app_subway/listar_sucursales.html', {'sucursales': sucursales})

def detalle_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    empleados_sucursal = Empleado.objects.filter(id_sucursal=sucursal)
    return render(request, 'app_subway/detalle_sucursal.html', {
        'sucursal': sucursal, 
        'empleados_sucursal': empleados_sucursal
    })

def crear_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_subway:listar_sucursales')
    else:
        form = SucursalForm()
    return render(request, 'app_subway/formulario_sucursal.html', {
        'form': form, 
        'titulo': 'Crear Sucursal'
    })

def editar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('app_subway:detalle_sucursal', id_sucursal=sucursal.id_sucursal)
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'app_subway/formulario_sucursal.html', {
        'form': form, 
        'titulo': 'Editar Sucursal'
    })

def borrar_sucursal(request, id_sucursal):
    sucursal = get_object_or_404(Sucursal, id_sucursal=id_sucursal)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('app_subway:listar_sucursales')
    return render(request, 'app_subway/confirmar_borrar_sucursal.html', {'sucursal': sucursal})

# Vistas para Empleados
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'app_subway/listar_empleados.html', {'empleados': empleados})

def detalle_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    return render(request, 'app_subway/detalle_empleado.html', {'empleado': empleado})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_subway:listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'app_subway/formulario_empleado.html', {
        'form': form, 
        'titulo': 'Crear Empleado'
    })

def editar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('app_subway:detalle_empleado', id_empleado=empleado.id_empleado)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'app_subway/formulario_empleado.html', {
        'form': form, 
        'titulo': 'Editar Empleado'
    })

def borrar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('app_subway:listar_empleados')
    return render(request, 'app_subway/confirmar_borrar_empleado.html', {'empleado': empleado})