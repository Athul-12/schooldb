from django.shortcuts import redirect, render
from . models import Teacher,AdminLogin
from teacher.models import student

# Create your views here.

def home(request):
    if "teacher_id" in request.session:
        t_session= Teacher.objects.get(id=request.session["teacher_id"])
        return render (request,'hom/sc_home.html',{'teacher_data':t_session})
    else:
        return redirect("teacher:teacher")

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
    studentss = student.objects.all()
    return render (request,'hom/view_student.html',{'student_lists':studentss})

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
