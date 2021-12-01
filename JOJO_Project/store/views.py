#from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Gateau
# Create your views here.
def index(request):
    message = "hello"
    return HttpResponse(message)

