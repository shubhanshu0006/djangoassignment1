from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contactus.html')

# Create your views here.
