from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Gateau, Contact, Booking


def index(request):
    gateaux = Gateau.objects.all()
    context = {'gateaux': gateaux}
    return render(request, 'store/index.html', context)

