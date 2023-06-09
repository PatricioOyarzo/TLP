from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

class Comunicado(models.Model):
    Nivel_Choices=[
        ("GEN", "General"),
        ("PRE", "Ciclo Preescolar"),
        ("BAS", "Ciclo Basico"),
        ("MED","Ciclo Medio")]
    titulo = models.TextField()
    detalle = models.TextField()
    nivel = models.CharField(choices=Nivel_Choices, max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
