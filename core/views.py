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

def login_view(request):
    return render(request, 'core/login.html', {'hide_layout': True})

def dashboard(request):
    return render(request, 'core/dashboard.html')

def grade_entry(request):
    return render(request, 'core/grade_entry.html')

def user_management(request):
    return render(request, 'core/user_management.html')

def digital_signature(request):
    return render(request, 'core/digital_signature.html')