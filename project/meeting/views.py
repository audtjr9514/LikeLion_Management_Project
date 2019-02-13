from django.shortcuts import render
from .models import Meet

# Create your views here.
def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def detail(request):
    return render(request, 'detail.html')