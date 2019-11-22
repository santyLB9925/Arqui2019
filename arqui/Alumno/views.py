from django.shortcuts import get_object_or_404
from django.http import Http404
from django_heroku import HerokuDiscoverRunner

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Alumno.models import Alumno
from Alumno.serializer import AlumnoSerializers


class AlumnoList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Alumno.objects.filter(delete = False)
        #many = True Si aplica si retorno multiples objetos
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class  AlumnoDetail(APIView):
    def get_object(self, rfid):
        try:
            return Alumno.objects.get(rfid=rfid, delete=False)
        except Alumno.DoesNotExist:
            return 404
    
    def get(self, request, rfid, format=None):
        alumno = self.get_object(rfid)
        if alumno != 404:
            #many = True No aplica si retorno un solo objeto
            serializer = AlumnoSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(alumno)
    
    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)




# Create your views here.
