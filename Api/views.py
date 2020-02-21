from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Excursion
from .serializers import ExcursionSerializer

class excursionView(ListAPIView):
    queryset = Excursion.objects.raw('SELECT * FROM Excursions')
    serializer_class = ExcursionSerializer

class singleExcursionView(RetrieveAPIView):
    serializer_class = ExcursionSerializer
    queryset = Excursion.objects.get(id=2)