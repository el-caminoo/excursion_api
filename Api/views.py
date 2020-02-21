from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Excursion
from .serializers import ExcursionSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully created new User')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class excursionView(ListAPIView):
    queryset = Excursion.objects.raw('SELECT * FROM Excursions')
    serializer_class = ExcursionSerializer
    permission_classes = (IsAuthenticated,)

class singleExcursionView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExcursionSerializer

    def get_queryset(self):
        query = self.kwargs['pk']
        return Excursion.objects.raw('SELECT * FROM Excursions WHERE id = %s', [query])


class editExcursionView(RetrieveUpdateAPIView):
    serializer_class = ExcursionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        query = self.kwargs['pk']
        return Excursion.objects.raw('SELECT * FROM Excursions WHERE id = %s', [query])

