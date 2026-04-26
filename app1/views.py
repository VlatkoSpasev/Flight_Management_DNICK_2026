from django.shortcuts import render
from .models import Flight

def index(request):
    all_flights = Flight.objects.all()
    context = {"flights": all_flights, "pageTitle": "Flight Application"}
    return render(request, 'index.html', context)