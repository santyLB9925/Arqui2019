from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellidoPaterno= models.CharField(max_length=254, null=False)
    apellidoMaterno= models.CharField(max_length=254, null=False)
    carrera = models.CharField(max_length=254, null=False)
    matricula= models.IntegerField(null=False)
    rfid = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Alumno'


