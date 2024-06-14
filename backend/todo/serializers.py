from rest_framework import serializers
from .models import Person, ToDo

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ToDoSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
