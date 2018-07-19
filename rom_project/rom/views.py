from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Hotel, Metro, Score
from .forms import SearchForm


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #search_result = form.search()

            metro = form.cleaned_data['city']
            arrival = form.cleaned_data['arrival']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            metro_id = Metro.objects.get(name=metro).id
            #return render(request, 'rom/results.html', {'form': form, 'search_result': search_result})
            return HttpResponseRedirect(reverse('rom:results', args=(metro_id,)))
    else:
        form = SearchForm()
    return render(request, 'rom/index.html', {'form': form})

def results(request, metro_id):
    metro = get_object_or_404(Metro, pk=metro_id)
    hotels = Hotel.objects.filter(metro=metro)
    context = {'metro': metro, 'hotels': hotels}
    return render(request, 'rom/results.html', context)


def detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'rom/detail.html', {'hotel': hotel})
