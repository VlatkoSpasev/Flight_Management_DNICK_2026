from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import FlightForm

from .models import Flight

def index(request):
    all_flights = Flight.objects.all()
    context = {"flights": all_flights, "pageTitle": "Flight Application"}
    return render(request, 'index.html', context)

@login_required
def details(request, id):
    try:
        flight = Flight.objects.get(id=id)
    except Flight.DoesNotExist:
        return index(request)
    data = {"flight": flight}
    return render(request, 'details.html', data)

@login_required
def add(request):
    if request.method == "POST":
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.save()
            return redirect('index')
    form = FlightForm()
    return render(request, 'add_flight.html', {"form":form})