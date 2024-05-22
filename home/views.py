from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def vision(request):
    return render(request, 'vision.html')

def mission(request):
    return render(request, 'mission.html')

def revenue(request):
    return render(request, 'revenue.html')

def more(request):
    return render(request, 'more.html')