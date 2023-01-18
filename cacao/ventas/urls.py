from django.urls import path
from django.http import HttpResponse


from ventas.views import saludar, listar_estudiantes, listar_profesores

urlpatterns = [
    path('lista/', listar_estudiantes),
    path('lista-profesores/', listar_profesores),
    path('saludar/', saludar),
]