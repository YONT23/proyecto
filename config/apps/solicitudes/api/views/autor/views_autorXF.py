from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import UsuarioXFormacion
from ...serializers.autor.autor_Serializers import UsuarioXFormacionSerializer

from django.shortcuts import get_object_or_404, render
from django.http import FileResponse
from django.views import View
from django.http import HttpResponse

class UsuarioXFormacionList(APIView):
    def get(self, request):
        usuarioxformacion = UsuarioXFormacion.objects.all()
        serializer = UsuarioXFormacionSerializer(usuarioxformacion, many=True)
        data = {'usuarioxformacion': serializer.data}
        return Response(data)

    def post(self, request):
        serializer = UsuarioXFormacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioXFormacionDetail(APIView):
    def get_object(self, pk):
        try:
            return UsuarioXFormacion.objects.get(pk=pk)
        except UsuarioXFormacion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        usuarioxformacion = self.get_object(pk)
        serializer = UsuarioXFormacionSerializer(usuarioxformacion)
        data = {'usuarioxformacion': serializer.data}
        return Response(data)

    def put(self, request, pk):
        usuarioxformacion = self.get_object(pk)
        serializer = UsuarioXFormacionSerializer(usuarioxformacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario_x_formacion = self.get_object(pk)
        if usuario_x_formacion is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        usuario_x_formacion.status = False  # Establecer el estado en "oculto"
        usuario_x_formacion.save()
        return Response(status=status.HTTP_204_NO_CONTENT)   

def descargar_archivo(request, archivo):
    if archivo:
        response = FileResponse(archivo)
        return response
    else:
        return HttpResponse("Archivo no encontrado", status=404)

def descargar_resol_conv(request, pk):
    contenido = get_object_or_404(UsuarioXFormacion, pk=pk, status=True)
    return descargar_archivo(request, contenido.resol_conv)

def descargar_cert_grado(request, pk):
    contenido = get_object_or_404(UsuarioXFormacion, pk=pk, status=True)
    return descargar_archivo(request, contenido.cert_grado)

def descargar_cert_resol(request, pk):
    contenido = get_object_or_404(UsuarioXFormacion, pk=pk, status=True)
    return descargar_archivo(request, contenido.cert_resol)



#def descargar_resol_conv(request, pk):
#    contenido = get_object_or_404(UsuarioXFormacion, pk=pk, status=True)
#    archivo = contenido.resol_conv
#    response = FileResponse(archivo)
#    return response
#
#def descargar_cert_grado(request, pk):
#    contenido = get_object_or_404(UsuarioXFormacion, pk=pk, status=True)
#    archivo = contenido.cert_grado
#    response = FileResponse(archivo)
#    return response
#
#def descargar_cert_resol(request, pk):
#    contenido = get_object_or_404(UsuarioXFormacion, pk=pk, status=True)
#    archivo = contenido.cert_resol
#    response = FileResponse(archivo)
#    return response
#