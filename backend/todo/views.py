from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Person, ToDo
from .serializers import PersonSerializer, ToDoSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'end_date', 'person']
