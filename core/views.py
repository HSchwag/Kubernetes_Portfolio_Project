from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

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