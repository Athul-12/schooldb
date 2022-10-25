from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'hom/master.html')

def student(request):
    return render (request,'hom/s_login.html')



