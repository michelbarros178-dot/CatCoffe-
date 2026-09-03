from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# --- IMPORTACIONES PARA EL CRUD ---
from .models import Gato, Adopcion
from .forms import GatoForm, AdopcionForm

# ==========================================
#              1. NAVEGACIÓN
# ==========================================

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def servicios(request):
    return render(request, 'paginas/servicios.html')

def porque_elegirnos(request):
    return render(request, 'paginas/porque_elegirnos.html')


# ==========================================
#             2. AUTENTICACIÓN
# ==========================================

def registro_view(request):
    if request.method == 'POST':
        u = request.POST.get('nombre') 
        e = request.POST.get('email')
        p = request.POST.get('password')

        if not u or User.objects.filter(username=u).exists():
            messages.error(request, "El usuario ya existe o no es válido.")
            return render(request, 'paginas/registro.html')

        # Crea el usuario e inicia sesión automáticamente
        nuevo_usuario = User.objects.create_user(username=u, email=e, password=p)
        nuevo_usuario.save()
        
        login(request, nuevo_usuario)
        return redirect('lista_gatos')

    return render(request, 'paginas/registro.html')

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('lista_gatos') 
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            
    return render(request, 'paginas/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/formulario.html', {'form': form, 'titulo_accion': f'Editar {producto.nombre}'})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminar.html', {'producto': producto})


# ==========================================
#           4. CRUD DE GATOS
# ==========================================

def lista_gatos(request):
    gatos = Gato.objects.all()
    return render(request, 'gatos/lista.html', {'gatos': gatos})

def crear_gato(request):
    if request.method == 'POST':
        # request.FILES es indispensable para poder capturar la foto física del miche
        form = GatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_gatos')
    else:
        form = GatoForm()
    return render(request, 'productos/formulario.html', {'form': form, 'titulo_accion': 'Registrar Nuevo Michi Resident 🐱'})

def editar_gato(request, pk):
    gato = get_object_or_404(Gato, pk=pk)
    if request.method == 'POST':
        form = GatoForm(request.POST, request.FILES, instance=gato)
        if form.is_valid():
            form.save()
            return redirect('lista_gatos')
    else:
        form = GatoForm(instance=gato)
    return render(request, 'productos/formulario.html', {'form': form, 'titulo_accion': f'Editar Datos de {gato.nombre}'})

def eliminar_gato(request, pk):
    gato = get_object_or_404(Gato, pk=pk)
    if request.method == 'POST':
        gato.delete()
        return redirect('lista_gatos')
    return render(request, 'productos/confirmar_eliminar.html', {'producto': gato})


# ==========================================
#         5. CRUD DE ADOPCIONES
# ==========================================

def lista_adopciones(request):
    adopciones = Adopcion.objects.all()
    return render(request, 'adopciones/lista.html', {'adopciones': adopciones})

def crear_adopcion(request):
    if request.method == 'POST':
        # request.FILES por si subes el contrato firmado en PDF
        form = AdopcionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_adopciones')
    else:
        form = AdopcionForm()
    return render(request, 'productos/formulario.html', {'form': form, 'titulo_accion': 'Registrar Nueva Adopción 📄'})

def eliminar_adopcion(request, pk):
    adopcion = get_object_or_404(Adopcion, pk=pk)
    if request.method == 'POST':
        adopcion.delete()
        return redirect('lista_adopciones')
    return render(request, 'productos/confirmar_eliminar.html', {'producto': adopcion})


# ==========================================
#     6. LISTAR USUARIOS (AUTH_USER)
# ==========================================

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})