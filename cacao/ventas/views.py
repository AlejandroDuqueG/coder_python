from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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