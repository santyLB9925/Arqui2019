# -------------AGREGANDO LIBRERIAS FRAMEWORK-----------
from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from Alumno.models import Alumno


class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('__all__')