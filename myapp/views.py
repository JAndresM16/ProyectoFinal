from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Usuario
from .models import Repuesto
from .models import Usuario
from .models import Revision
from django.contrib.auth.decorators import login_required

def login(request):
    
    if request.method == 'POST':        
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        informacion = Usuario.objects.filter(usuario=usuario, contraseña=contraseña)
        if informacion.exists():
            return render(request, 'informacion.html', {'informacion':informacion})
    return render (request, 'Login.html')

def registro(request):
    if request.method == 'POST':
        nuevo_usuario = Usuario(usuario=request.POST['usuario'], nombre=request.POST['nombre'], telefono=request.POST['telefono'], 
                                edad=request.POST['edad'], pais=request.POST['pais'], contraseña=request.POST['contraseña'])
        nuevo_usuario.save()
        return HttpResponseRedirect('/login/')
    return render(request, 'registro.html')

def informacion(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'informacion.html', {'repuestos': repuestos})

def Adventure(request):
    return render(request, 'Adventure.html')

def Deportiva(request):
    return render(request, 'Deportiva.html')

def Enduro(request):
    return render(request, 'Enduro.html')

def Hyper(request):
    return render(request, 'Hyper.html')

def Scooter(request):
    return render(request, 'Scooter.html')

def Urbana(request):
    return render(request, 'Urbana.html')

def Usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'Usuario.html', {'usuarios': usuarios})


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuario.usuario = request.POST['usuario']
        usuario.nombre = request.POST['nombre']
        usuario.telefono = request.POST['telefono']
        usuario.edad = request.POST['edad']
        usuario.pais = request.POST['pais']
        usuario.contraseña = request.POST['contraseña']
        usuario.save()
        # Actualiza la redirección a la vista que lista los usuarios
        return redirect('Usuarios')  # Actualiza esto con el nombre de tu URL de lista de usuarios

    usuarios = Usuario.objects.all()
    return render(request, 'Usuario.html', {'usuarios': usuarios, 'usuario_editar': usuario})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('Usuarios')

def Repuestos(request):
    if request.method == 'POST':
        nuevo_repuesto = Repuesto(
            nombre=request.POST['nombre'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            marca=request.POST['marca'],
            tipo_moto=request.POST['tipo_moto']
        )
        nuevo_repuesto.save()
        return redirect('Repuestos')  # Redirige para evitar el reenvío del formulario al recargar la página

    repuestos = Repuesto.objects.all()

    return render(request, 'Repuestos.html', {'repuestos': repuestos} )

def editar_repuesto(request, repuesto_id):
    repuesto = get_object_or_404(Repuesto, id=repuesto_id)

    if request.method == 'POST':
        repuesto.nombre = request.POST['nombre']
        repuesto.precio = request.POST['precio']
        repuesto.stock = request.POST['stock']
        repuesto.marca = request.POST['marca']
        repuesto.tipo_moto = request.POST['tipo_moto']
        repuesto.save()
        return redirect('Repuestos')

    repuestos = Repuesto.objects.all()
    return render(request, 'Repuestos.html', {'repuestos': repuestos, 'repuesto_editar': repuesto})

def eliminar_repuesto(request, repuesto_id):
    repuesto = get_object_or_404(Repuesto, id=repuesto_id)
    repuesto.delete()
    return redirect('Repuestos')

def Revisiones(request):
    if request.method == 'POST':
        nuevo_revision = Revision(
            codigo=request.POST['codigo'],
            C_filtro=request.POST['C_filtro'],
            C_aceite=request.POST['C_aceite'],
            C_freno=request.POST['C_freno'],
            Revision_vehiculo=request.POST['Revision_vehiculo']
        )
        nuevo_revision.save()
        return redirect('Revisiones') 

    revisiones = Revision.objects.all()

    return render(request, 'Revisiones.html', {'revisiones': revisiones} )

def editar_revisiones(request, revisiones_id):
    revision = get_object_or_404(Revision, id=revisiones_id)

    if request.method == 'POST':
        revision.codigo = request.POST['codigo']
        revision.C_filtro = request.POST['C_filtro']
        revision.C_aceite = request.POST['C_aceite']
        revision.C_freno = request.POST['C_freno']
        revision.Revision_vehiculo = request.POST['Revision_vehiculo']
        revision.save()
        return redirect('Revisiones')

    revisiones = Revision.objects.all()
    return render(request, 'Revisiones.html', {'revisiones': revisiones, 'revisiones_editar': revision})

def eliminar_revisiones(request, revisiones_id):
    revision = get_object_or_404(Revision, id=revisiones_id)
    revision.delete()
    return redirect('Revisiones')

def Comprar_repuesto(request):
    if request.method == 'POST':
        repuesto_id = request.POST['repuesto_id']
        repuesto = Repuesto.objects.get(id=repuesto_id)

        if repuesto.stock > 0:
            repuesto.stock -= 1
            repuesto.save()

    repuestos = Repuesto.objects.all()
    return render(request, 'Comprar_repuesto.html', {'repuestos': repuestos})

#python manage.py runserver