from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField()
    fecha_inicio = forms.DateField(null=True)
    descripcion = forms.TextField(null=True)


class EstudianteFormulario(forms.Form):   
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=32)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    profesion = forms.CharField(max_length=128)
    bio = forms.TextField()


class ProfesorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=32)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(null=True)
    profesion = forms.CharField(max_length=128)
    bio = forms.TextField(null=True)


class EntregableFormulario(forms.Form):   
    nombre = forms.CharField(max_length=256)
    fecha_entrega = forms.DateTimeField()
    esta_aprobado = forms.BooleanField(default=False)