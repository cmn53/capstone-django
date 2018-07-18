from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Hotel, Metro, Score

def index(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'rom/index.html', context)

def detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'rom/detail.html', {'hotel': hotel})

def results(request, metro_id):
    metro = get_object_or_404(Metro, pk=metro_id)
    hotels = Hotel.objects.filter(metro=metro)
    context = {'metro': metro, 'hotels': hotels}
    return render(request, 'rom/results.html', context)
