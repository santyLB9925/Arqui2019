from django.db import models
from django.utils import timezone
from Alumno.models import Alumno
from  datetime import datetime

class Asistencia(models.Model):
    myNow=datetime.now()
    fechaModificada= myNow.strftime("%Y%m%d")
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha=models.DateTimeField(default=timezone.now)
    fechaCompare = models.IntegerField(default=fechaModificada)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Asistencia'

# Create your models here.
