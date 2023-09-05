from ....serializer.serializers import PersonsSerializers
from apps.authenticacion.models import Persons
from rest_framework import status
from rest_framework.views import APIView
from .....mudules import ListAPIView, CreateAPIView, UpdateAPIView, Response, create_response
from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework.generics import RetrieveUpdateAPIView

class PersonView(ListAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializers = PersonsSerializers(data, many=True)
        response, code = create_response(
            status.HTTP_200_OK, 'Person', serializers.data)
        return Response(response, status=code)

class PersonCreateView(CreateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

    def post(self, request, *args, **kwargs):
        personSerializers = PersonsSerializers(data=request.data)
        if personSerializers.is_valid():
            personSerializers.save()
            response, code = create_response(
                status.HTTP_200_OK, 'Person', personSerializers.data)
            return Response(response, status=code)
        response, code = create_response(
            status.HTTP_400_BAD_REQUEST, 'Error', personSerializers.errors)
        return Response(response, status=code)

class PersonUpdateView(RetrieveUpdateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonsSerializers

class PersonDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            person = Persons.objects.get(pk=pk)
        except Persons.DoesNotExist:
            return Response({"detail": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if status is True before deleting
        if person.status:
            person.status = False
            person.save()
            return Response({"detail": "Person hidden successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Person is already hidden"}, status=status.HTTP_400_BAD_REQUEST)