from django.db import models
from django.contrib.auth.models import User

# 1. Tabla de Gatos (Los protagonistas del café)
class Gato(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='gatos/', null=True, blank=True)
    disponible_adopcion = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# 2. Tabla de Productos (Comida, Café, etc.)
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50) # Ej: Bebidas, Repostería

    def __str__(self):
        return self.nombre

# 3. Módulo de Adopciones (Seguimiento legal)
class Adopcion(models.Model):
    # Relaciona con el gato y con el cliente (User de Django)
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()
    # Guarda la ruta del PDF del contrato
    documento_contrato_url = models.FileField(upload_to='contratos/', null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Adopción de {self.gato.nombre} por {self.cliente.username}"