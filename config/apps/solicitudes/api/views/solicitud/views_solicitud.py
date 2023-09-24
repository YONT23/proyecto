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

from apps.authenticacion.models import CustomUser

class SolicitudList(generics.ListCreateAPIView):
    queryset = Solicitud.objects.filter(status=True)  # Filtrar por status=True
    serializer_class = SolicitudSerializer

    def create(self, request, *args, **kwargs):
        # Obtén una copia mutable de los datos del formulario
        solicitud_data = request.data.copy()

        # Asegura que 'autores' esté presente en los datos de la solicitud
        autores_data = solicitud_data.get('autores', [])

        serializer = self.get_serializer(data=solicitud_data)

        if serializer.is_valid():
            # Guarda la solicitud sin los autores
            solicitud = serializer.save()

            # Ahora, vincula los autores con la solicitud
            for autor_id in autores_data:
                autor = CustomUser.objects.get(pk=autor_id)
                solicitud.autores.add(autor)

            # Devuelve la respuesta
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
        autores_data = CustomUser.objects.values('id', 'email')

        print("La función se ha ejecutado correctamente")  # Verifica si se ejecuta la función
        subject = 'Nueva solicitud de revisión de artículo'
        message = 'Se ha creado una nueva solicitud de revisión de artículo.'
        from_email = 'mendozaym01@gmail.com'
        
        recipient_list = [autor['email'] for autor in autores_data] + ['lordym00@gmail.com']

        send_mail(subject, message, from_email, recipient_list)








