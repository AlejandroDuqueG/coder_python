from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from ventas.models import Estudiante, Profesor, Curso

def saludar(request):
    return HttpResponse(f'Hola, esto es una prueba!. Hora: {datetime.now()}')

def inicio(request):
    return render(
        request=request,
        template_name='ventas/inicio.html',
    )

def listar_estudiantes(request):
    contexto = {
        'estudiantes': ['Alejandro', 'Belisario', 'Fernando']
    }
    return render(
        request=request, 
        template_name='ventas/lista_estudiantes.html',
        context=contexto
        )

def listar_profesores(request):
    return render(request=request, template_name='ventas/lista_profesores.html')

def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='ventas/lista_cursos.html',
        context=contexto,
    )

def crear_curso(request):
    """No se usa"""
    if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:  # GET
        return render(
            request=request,
            template_name='ventas/formulario_curso.html',
        )

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(comision__exact=data['busqueda'])
        )
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )