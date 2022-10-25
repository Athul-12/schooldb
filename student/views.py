from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'hom/home.html')

def profile(request):
    return render (request,'hom/profile.html')

def pas(request):
    return render (request,'hom/chngpas.html')