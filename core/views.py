from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
import socket

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    return render(request, 'home.html', {'hostname': hostname})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def healthz(request):
    return HttpResponse("OK", content_type="text/plain")

def metrics(request):
    # Example metrics data
    metrics_data = "app_requests_total 1024\napp_errors_total 12"
    return HttpResponse(metrics_data, content_type="text/plain")