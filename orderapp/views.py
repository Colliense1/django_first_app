from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def order(request):
    return render (request, "orders.html")

def global_home(request):
    return HttpResponse("Homepage Content...")