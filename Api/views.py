from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from .models import Excursion
from .serializers import ExcursionSerializer, userSerializer
from django.contrib.auth.models import User


class userView(ListAPIView):
    serializer_class = userSerializer
    queryset = User.objects.all()


class excursionView(ListAPIView):
    queryset = Excursion.objects.raw('SELECT * FROM Excursions')
    serializer_class = ExcursionSerializer

class singleExcursionView(RetrieveAPIView):
    serializer_class = ExcursionSerializer

    def get_queryset(self):
        query = self.kwargs['pk']
        return Excursion.objects.raw('SELECT * FROM Excursions WHERE id = %s', [query])


class editExcursionView(RetrieveUpdateAPIView):
    serializer_class = ExcursionSerializer

    def get_queryset(self):
        query = self.kwargs['pk']
        return Excursion.objects.raw('SELECT * FROM Excursions WHERE id = %s', [query])

