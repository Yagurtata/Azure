from django.shortcuts import render, redirect
from .models import Crucero, Destination
from .forms import CruceroForm

def index(request):
    cruceros = Crucero.objects.all()
    destinos = Destination.objects.all() 
    if request.method == 'POST':
        form = CruceroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CruceroForm()

    return render(request, 'index.html', {'cruceros': cruceros,  'destinos': destinos, 'form': form})

def about(request):
    return render(request, 'about.html')  # No es necesario cambiar esto
