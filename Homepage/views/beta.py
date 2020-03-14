from django.shortcuts import render
from Homepage.models import Produkty

def home(request):
    zmiennaprodukty = Produkty.objects
    return render(request, 'home.html', {'produkty':zmiennaprodukty})


def homeles(request, id):
    obj = Produkty.objects.get(id=id)
    zmiennaprodukty = Produkty.objects

    return render(request, 'opisproduktu.html', {'objekty':obj, 'produkty':zmiennaprodukty})


def polityka(request):

    return render(request, 'politykaprywatnosci.html')