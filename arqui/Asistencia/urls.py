from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Asistencia import views

urlpatterns = [
    re_path(r'asistencia_lista/$', views.AsistenciaList.as_view()),
    re_path(r'asistencia_detail/(?P<idAlumno>\d+)/$',views.AsistenciaDetail.as_view()),
    re_path(r'asistencia_filtrado/(?P<idAlumno>\d+)/$',views.AsistenciaFiltrado.as_view()),
]