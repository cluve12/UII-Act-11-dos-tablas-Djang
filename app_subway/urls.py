from django.urls import path
from . import views

app_name = 'app_subway'
urlpatterns = [
    # Rutas para Sucursales (principal del sitio)
    path('', views.listar_sucursales, name='listar_sucursales'),
    path('sucursales/', views.listar_sucursales, name='listar_sucursales'),
    path('sucursal/crear/', views.crear_sucursal, name='crear_sucursal'),
    path('sucursal/<int:id_sucursal>/', views.detalle_sucursal, name='detalle_sucursal'),
    path('sucursal/editar/<int:id_sucursal>/', views.editar_sucursal, name='editar_sucursal'),
    path('sucursal/borrar/<int:id_sucursal>/', views.borrar_sucursal, name='borrar_sucursal'),
    
    # Rutas para Empleados
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleado/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleado/<int:id_empleado>/', views.detalle_empleado, name='detalle_empleado'),
    path('empleado/editar/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('empleado/borrar/<int:id_empleado>/', views.borrar_empleado, name='borrar_empleado'),
]