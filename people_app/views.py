from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
