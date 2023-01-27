from django.urls import path
from django.http import HttpResponse


from ventas.views import (
    saludar, listar_estudiantes, listar_profesores, listar_cursos, crear_curso)

urlpatterns = [
    path('lista-alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('lista-cursos/', listar_cursos, name="listar_cursos"),
    path('lista-profesores/', listar_profesores, name="listar_profesores"),
    path('saludar/', saludar),
    path('crear-curso/', crear_curso, name="crear_curso")
]