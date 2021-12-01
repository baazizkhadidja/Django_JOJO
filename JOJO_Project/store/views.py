from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Gateau, Contact, Booking


def index(request):
    albums = Album.objects.filter(available = True).order_by('-created_at')[:12]
    context = {'albums': albums}
    return render(request, 'store/index.html', context)

