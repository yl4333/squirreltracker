from django.shortcuts import render
from django.http import HttpResponse
from sightings.models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels[:99]
    }
    return render(request, 'map.html', context)
