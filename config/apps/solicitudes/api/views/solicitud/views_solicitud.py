from django.http import Http404

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from ....models import Solicitud
from ...serializers.solicitud.solicitud_serializers import SolicitudSerializer
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response

class SolicitudList(generics.ListCreateAPIView):
    queryset = Solicitud.objects.filter(status=True)  # Filtrar por status=True
    serializer_class = SolicitudSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status:
            serializer = self.get_serializer(instance)
            data = {'solicitud': serializer.data}
            return Response(data)
        else:
            return Response('No encontrado', status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        # Cambiar el estado booleano en lugar de eliminar el objeto
        instance.status = False
        instance.save()
    
@receiver(post_save, sender=Solicitud)
def enviar_correo_cuando_se_crea_solicitud(sender, instance, created, **kwargs):
    if created:
        subject = 'Nueva solicitud de revisión de artículo'
        message = 'Se ha creado una nueva solicitud de revisión de artículo.'
        from_email = 'mendozaym01@gmail.com'
        # A continuación, agrega las direcciones de correo electrónico de los destinatarios, por ejemplo, los editores jefe
        recipient_list = ['lordym00@gmail.com', instance.autor.email]

        send_mail(subject, message, from_email, recipient_list)
