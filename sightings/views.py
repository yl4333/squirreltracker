from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm


def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels':squirrels
    }
    return render(request, 'index.html', context)

def stats(request, squirrelid):
    squirrel = Squirrel.obejects.get(id = squirrelid)
    return HttpResponse(squirrel.color)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        #chech data with form
        if form.is_valid():
            form.save()
            return redirect(f'sightings/')
    else:
        form = SquirrelForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'add.html', context)


def update(request, squirrelid):
    squirrel = Squirrel.objects.get(id=squirrelid)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        #check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrelid}')
    else:
        form = PetForm(instance=squirrel)
    
    context = {
        'form': form,
    }
    
    return render(request, 'sightings/update.html', context)




