# Generated by Django 4.1.5 on 2023-02-03 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('dni', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('profesion', models.CharField(max_length=128)),
                ('bio', models.TextField(null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiantes',
            new_name='Estudiante',
        ),
        migrations.AddField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]
