from django.shortcuts import redirect, render
from . models import Teacher,AdminLogin
from teacher.models import student
from django.http import JsonResponse
# Create your views here.

def home(request):
        
        return render (request,'hom/sc_home.html')

def AddTeach(request):
    if request.method == 'POST':
        tname = request.POST['tname']
        tmail = request.POST['tmail']
        taddress = request.POST['taddress']
        tquali = request.POST['tquali']
        tgender = request.POST['tgender']
        texp = request.POST['texp']
        tphoto = request.FILES['tphoto']
        tpass = request.POST['tpass']
        tdob = request.POST['tdob']
        teacher = Teacher(name = tname, email = tmail,
        qualification = tquali, exp = texp, gender = tgender,
        dob = tdob,password = tpass, photo = tphoto, address = taddress)

        teacher.save()
    return render (request,'hom/add_teach.html')

def viewstudent(request):
    students = student.objects.all()
    return render (request,'hom/view_student.html',{'student_list':students})

def ViewTeach(request):
    teachers = Teacher.objects.all()
    return render (request,'hom/view_teach.html',{'teacher_list':teachers})

def ChngPas(request):
    return render (request,'hom/changepass.html')

def adm(request):
    if request.method == 'POST':
        adminusername = request.POST['uname']
        adminpassword = request.POST['a_pass']

        try:
            adminlogin = AdminLogin.objects.get(admin_username = adminusername,admin_password = adminpassword)  
            return redirect("sc_admin:a_home") 

        except:
            msg = 'invalid user name and password'
            return render (request,"hom/a_login.html",{"error_messege" : msg})
    return render (request,'hom/a_login.html')

def email_exist(request):
    emaile = request.POST['email']
    emailex = Teacher.objects.filter(email = emaile).exists()
    return JsonResponse ({'status':emailex})


def fnAngularTest(req):
    return JsonResponse({'data': "abcdef"})
