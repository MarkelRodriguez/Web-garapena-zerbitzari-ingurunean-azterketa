
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Alokairua, Etxea, Pertsona
# Create your views here.
def index(request):

    alokairuak = Alokairua.objects.all

    return render(request, 'index.html', {'alokairuak':alokairuak })

def pertsona(request):

    pertsonak = Pertsona.objects.all

    return render(request, 'pertsona.html', {'pertsonak':pertsonak })

def etxea(request):

    etxeak = Etxea.objects.all

    return render(request, 'etxea.html', {'etxeak':etxeak })

def gehitualokairua(request):
    pertsonak = Pertsona.objects.all
    etxeak = Etxea.objects.all
    return render(request, 'alokairuagehitu.html', {'pertsonak':pertsonak, 'etxeak':etxeak})

def gehituerregistroalokairua(request):
    pertsonaid = request.POST['pertsona']
    pertsona = Pertsona.objects.get(dni=pertsonaid)
    etxeaid = request.POST['etxea']
    etxea= Etxea.objects.get(id=etxeaid)
    hasiera_data = request.POST['alokairu_data_hasi']
    bukaera_data = request.POST['alokairu_data_bukatu']

    alokairua= Alokairua(pertsona=pertsona, etxea=etxea, alokairu_data_hasi=hasiera_data, alokairu_data_bukatu=bukaera_data)
    alokairua.save()
    return HttpResponseRedirect(reverse('index'))

def gehitupertsona(request):
    return render(request, 'pertsonagehitu.html')

def gehituerregistropertsona(request):
    dni = request.POST['dni']
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    emaila = request.POST['emaila']

    pertsona = Pertsona(dni=dni, izena=izena, abizena=abizena, emaila=emaila)
    pertsona.save()
    return HttpResponseRedirect(reverse('pertsona'))

def gehituetxea(request):
    return render(request, 'etxeagehitu.html')

def gehituerregistroetxea(request):
    izena = request.POST['izena']
    herria = request.POST['herria']
    pertsonakop = request.POST['pertsonakop']
    

    etxea = Etxea( izena=izena, herria=herria, pertsona_kop=pertsonakop)
    etxea.save()
    return HttpResponseRedirect(reverse('etxea'))

def ezabatupertsona(request, dni):
    pertsona = Pertsona.objects.get(dni=dni)
    pertsona.delete()
    return HttpResponseRedirect(reverse('pertsona'))

def eguneratupertsona(request, dni):
    pertsona = Pertsona.objects.get(dni=dni)
    return render(request, 'eguneratupertsona.html', {'pertsona': pertsona})

def eguneratuerregistropertsona(request, dni):
    dni = request.POST['dni']
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    emaila = request.POST['emaila']
    pertsona = Pertsona.objects.get(dni=dni)
    pertsona.dni = dni
    pertsona.izena = izena
    pertsona.abizena = abizena
    pertsona.emaila = emaila
    pertsona.save()
    return HttpResponseRedirect(reverse('pertsona'))


def ezabatuetxea(request, id):
    etxea = Etxea.objects.get(id=id)
    etxea.delete()
    return HttpResponseRedirect(reverse('pertsona'))

def eguneratuetxea(request, id):
    etxea = Etxea.objects.get(id=id)
    return render(request, 'eguneratuetxea.html', {'etxea': etxea})

def eguneratuerregistroetxea(request, id):
    
    izena = request.POST['izena']
    herria = request.POST['herria']
    pertsonakop = request.POST['pertsonakop']
    etxea = Etxea.objects.get(id=id)
    
    etxea.izena = izena
    etxea.herria = herria
    etxea.pertsona_kop = pertsonakop
    etxea.save()
    return HttpResponseRedirect(reverse('etxea'))