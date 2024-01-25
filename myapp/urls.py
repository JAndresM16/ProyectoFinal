from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('informacion/', views.informacion, name='informacion'),
    path('Adventure/', views.Adventure, name='Adventure'),
    path('Deportiva/', views.Deportiva, name='Deportiva'),
    path('Enduro/', views.Enduro, name='Enduro'),
    path('Scooter/', views.Scooter, name='Scooter'),
    path('Urbana/', views.Urbana, name='Urbana'),
    path('Hyper/', views.Hyper, name='Hyper'),
    path('Usuarios/', views.Usuarios, name='Usuarios'),
    path('Revisiones/', views.Revisiones, name='Revisiones'),
    path('Repuestos/', views.Repuestos, name='Repuestos'),
    path('editar_repuesto/<int:repuesto_id>/', views.editar_repuesto, name='editar_repuesto'),
    path('eliminar_repuesto/<int:repuesto_id>/', views.eliminar_repuesto, name='eliminar_repuesto'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('editar_revisiones/<int:revisiones_id>/', views.editar_revisiones, name='editar_revisiones'),
    path('eliminar_revisiones/<int:revisiones_id>/', views.eliminar_revisiones, name='eliminar_revisiones'),
    path('Comprar_Repuesto/', views.Comprar_repuesto, name='Comprar_Repuesto'),


]
