from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Squirrel
from .forms import SquirrelForm


def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'index.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    context={
        'squirrels':squirrels   
    }
    return render(request, 'stats.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        #chech data with form
        print(form.errors)
        if form.is_valid():
            form.save()
            print("Added!")
            return redirect('/sightings/')
    else:
        print("Not adding")
        form = SquirrelForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'add.html', context)


def update(request, squirrelid=None):
    squirrel = Squirrel.objects.get(squirrelid=squirrelid)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        #check data with form
        if form.is_valid():
            form.save()
            return redirect('/sightings/' + squirrelid)
    else:
        form = SquirrelForm(instance=squirrel)
    
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)




