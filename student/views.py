from django.shortcuts import redirect, render
from teacher.models import student
from . decorations import auth_student
import logging


# logger = logging.getLogger('django')


# Create your views here.
@auth_student
def home(request):
    students = student.objects.get(id = request.session['student_id'])
    
    return render (request,'hom/home.html',{'student_data':students})
@auth_student
def profile(request):
    return render (request,'hom/profile.html')
@auth_student
def pas(request):
    return render (request,'hom/chngpas.html')

def students(request):
    msg = ""
    if request.method == 'POST':

        studentname = request.POST['sname']
        studentpass = request.POST['spass']

        try :
            studentlogin = student.objects.get(s_name = studentname,s_password = studentpass)
            request.session["student_id"] = studentlogin.id
            return redirect("student:s_home")

        except:
            msg = 'invalid username or password'
    return render (request,'hom/s_login.html',{'status':msg})

def log_out(request):
    del request.session ['student_id']
    request.session.flush()
    return redirect ('common:home')

