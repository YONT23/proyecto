from django.http import Http404

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import FileResponse

from ....models import Seguimiento
from ...serializers.seguimiento.seguimiento_serializers import SeguimientoSerializer
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from apps.authenticacion.models import CustomUser

class SeguimientoList(generics.ListCreateAPIView):
    queryset = Seguimiento.objects.filter(status=True)  
    serializer_class = SeguimientoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeguimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seguimiento.objects.filter(status=True)
    serializer_class = SeguimientoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status:
            serializer = self.get_serializer(instance)
            data = {'seguimiento': serializer.data}
            return Response(data)
        else:
            return Response('No encontrado... Realice otra búsqueda.', status=status.HTTP_404_NOT_FOUND)

    def perform_update(self, serializer):
        instance = self.get_object()

        if (
            self.request.data.get('fecha_asignacion') or
            self.request.data.get('fecha_evaluacion') or
            self.request.data.get('estado_seguimiento')
        ):
            # Si se están actualizando campos relevantes, establece cambio_relevante en True
            instance.cambio_relevante = True

        serializer.save()  # Guarda la instancia actualizada

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()

def descargar_archivo(request, pk):
    seguimiento = get_object_or_404(Seguimiento, pk=pk, status=True)
    archivo = seguimiento.correciones
    if archivo:
        response = FileResponse(archivo)
        return response
    else:
        raise Http404("Archivo no encontrado")

@receiver(post_save, sender=Seguimiento)
def enviar_correo_cuando_actualiza(sender, instance, **kwargs):
    if instance.cambio_relevante:
        autores_data = CustomUser.objects.values('id', 'email')
        subject = 'Seguimiento de su solicitud generada'
        message = 'Tu seguimiento de su solicitud ha sido generada exitosamente'
        from_email = 'mendozaym01@gmail.com'
        
        recipient_list = [autor['email'] for autor in autores_data] + [instance.responsableId.email]
        send_mail(subject, message, from_email, recipient_list)

        instance.cambio_relevante = False
        instance.save()
