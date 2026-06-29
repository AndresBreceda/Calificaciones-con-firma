from django.shortcuts import render, redirect
from .forms import RegistroForm

def index(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistroForm()
        
    return render(request, 'core/index.html', {'form': form})