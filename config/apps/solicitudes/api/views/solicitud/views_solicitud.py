from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ....models import Solicitud
from ...serializers.solicitud.solicitud_serializers import SolicitudSerializer

from rest_framework.response import Response

#from django.contrib.auth.decorators import user_passes_test
#from django.utils.decorators import method_decorator
#from configs.middlewares.roles_middleware import RoleMiddleware



#def is_author(user):
#    return user.role == 'Autor'
#
#@method_decorator(RoleMiddleware, name='dispatch')
#class SolicitudDetail(APIView):
#    def get_object(self, pk):
#        try:
#            return Solicitud.objects.get(pk=pk)
#        except Solicitud.DoesNotExist:
#            raise Http404
#
#    def get(self, request, pk):
#        solicitud = self.get_object(pk)
#        serializer = SolicitudSerializer(solicitud)
#        data = {'solicitud': serializer.data}
#        return Response(data)
#
#    @method_decorator(user_passes_test(lambda user: not is_author(user)))
#    def post(self, request):
#        serializer = SolicitudSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    @method_decorator(user_passes_test(lambda user: not is_author(user)))
#    def put(self, request, pk):
#        solicitud = self.get_object(pk)
#        serializer = SolicitudSerializer(solicitud, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    @method_decorator(user_passes_test(lambda user: not is_author(user)))
#    def delete(self, request, pk):
#        solicitud = self.get_object(pk)
#        solicitud.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#

class SolicitudList(APIView):
    def get(self, request, format=None):
        solicitudes = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitudes, many=True)
        data = {'solicitudes': serializer.data}
        return Response(data)

    def post(self, request, format=None):
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SolicitudDetail(APIView):
    def get_object(self, pk):
        try:
            return Solicitud.objects.get(pk=pk)
        except Solicitud.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        serializer = SolicitudSerializer(solicitud)
        data = {'solicitud': serializer.data}
        return Response(data)

    def put(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        serializer = SolicitudSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        solicitud = self.get_object(pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

