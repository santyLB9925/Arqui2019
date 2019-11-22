from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from  datetime import datetime

from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers

class AsistenciaList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Asistencia.objects.filter(delete = False)
        #many = True Si aplica si retorno multiples objetos
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsistenciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class  AsistenciaDetail(APIView):
    def get_object(self, idAlumno):
        try:
            return Asistencia.objects.get(idAlumno=idAlumno, delete=False)
        except Asistencia.DoesNotExist:
            return 404
    
    def get(self, request, idAlumno, format=None):
        Asistencia = self.get_object(id)
        if Asistencia != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = AsistenciaSerializers(Asistencia)
            return Response(serializer.data)
        else:
            return Response(Asistencia)
    
    def put(self, request, idAlumno, format=None):
        Asistencia = self.get_object(idAlumno)
        if Asistencia != 404:
            serializer = AsistenciaSerializers(Asistencia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
class  AsistenciaFiltrado(APIView):
    def get_object(self, idAlumno):
        try:
            queryset=Asistencia.objects.filter(idAlumno=idAlumno,delete=False).count()
            queryset2 = Asistencia.objects.filter(idAlumno=idAlumno,delete=False).latest('fecha')
            return queryset2
        except Asistencia.DoesNotExist:
            return 404
    
    def get(self, request, idAlumno, format=None):
        Asistencia = self.get_object(idAlumno)
        if Asistencia != 404:
            serializer = AsistenciaSerializers(Asistencia)
            serializer2=serializer.data['fechaCompare']
            print(serializer2)
            myNow=datetime.now()
            fechaModificada= myNow.strftime("%Y%m%d")
            print(fechaModificada)
            if serializer2==int (fechaModificada):
                return Response (1)
            else:
                 return Response(0)
        else:
            return Response(0)
    def post(self, request, format=None):
        serializer = AsistenciaSerializers(data = request.data)
        print
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Create your views here.

