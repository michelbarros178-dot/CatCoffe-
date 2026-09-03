from django.urls import path
from . import views

urlpatterns = [
    # --- Rutas de Navegación del Sitio Público ---
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('por-que-elegirnos/', views.porque_elegirnos, name='porque_elegirnos'),

    # --- Rutas de Autenticación ---
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),



    # --- TABLA 2: CRUD de Gatos (`productos_gato`) ---
    path('gatos/', views.lista_gatos, name='lista_gatos'),
    path('gatos/nuevo/', views.crear_gato, name='crear_gato'),
    path('gatos/editar/<int:pk>/', views.editar_gato, name='editar_gato'),
    path('gatos/eliminar/<int:pk>/', views.eliminar_gato, name='eliminar_gato'),

    # --- TABLA 3: CRUD de Adopciones (`productos_adopcion`) ---
    path('adopciones/', views.lista_adopciones, name='lista_adopciones'),
    path('adopciones/nueva/', views.crear_adopcion, name='crear_adopcion'),
    path('adopciones/eliminar/<int:pk>/', views.eliminar_adopcion, name='eliminar_adopcion'),

    # --- TABLA 4: Listar Usuarios Registrados (`auth_user`) ---
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]