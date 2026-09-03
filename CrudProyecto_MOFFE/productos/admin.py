from django.contrib import admin
from .models import Gato, Producto, Adopcion

# Configuración para ver más detalles de los gatos en la lista
class GatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'edad', 'disponible_adopcion')
    list_filter = ('disponible_adopcion', 'raza')
    search_fields = ('nombre', 'raza')

# Configuración para el menú del café
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre',)

# Configuración para el módulo legal de adopciones
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('gato', 'cliente', 'fecha_entrega', 'fecha_registro')
    list_filter = ('fecha_entrega',)
    # Esto ayuda a buscar por nombre de gato o nombre de usuario
    search_fields = ('gato__nombre', 'cliente__username')

# Registro de los modelos
admin.site.register(Gato, GatoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Adopcion, AdopcionAdmin)