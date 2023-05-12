from django.http import Http404

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import PasosSolicitud
from ...serializers.solicitud.solicitud_serializers import PasosSolicitudSerializer

class PasosSolicitudList(generics.ListCreateAPIView):
    queryset = PasosSolicitud.objects.all()
    serializer_class = PasosSolicitudSerializer

class PasosSolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PasosSolicitud.objects.all()
    serializer_class = PasosSolicitudSerializer