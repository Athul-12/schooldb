from sys import dont_write_bytecode
from django.shortcuts import redirect, render
from sc_admin.models  import Teacher
from . models import student
from . decoration import auth_teacher

# Create your views here.
@auth_teacher
def home(request):
    teacher = Teacher.objects.get(id = request.session['teacher_id'])
    
    return render (request,'hom/t_home.html',{'teacher_data':teacher})
@auth_teacher
def profil(request):
    return render (request,'hom/t_profile.html')
@auth_teacher
def addstudent(request):
    if request.method == 'POST':
        name = request.POST['sname']
        uname = request.POST['uname']
        add = request.POST['add']
        gender = request.POST['gender']
        dob = request.POST['dob']
        pas = request.POST['pas']
        photo = request.FILES['photo']
        students = student(s_name = name ,
        s_uname = uname,
        s_gender = gender,
        s_dob = dob,
        s_password = pas,
        s_photo = photo,
        s_address = add,
        teacher_id = request.session['teacher_id'])

        students.save()
    return render (request,'hom/addstudent.html')
@auth_teacher
def chnge(request):
    msg = ""
    if request.method == 'POST':
        t_old_psw = request.POST['old']
        t_new_psw = request.POST['pass1']
        t_con_psw = request.POST['pass2']
        teacher = Teacher.objects.get(id=request.session['teacher_id'])

        if teacher.password == t_old_psw :
            if t_new_psw == t_con_psw:
                # Teacher.objects.filter(id = request.session['teacher_id']).update(password = t_new_psw)
                teacher.password = t_new_psw
                teacher.save()
                msg = "password changed successfully"
            else:
                msg = "password mismatch"
        else:
            msg = "incorrect password"
    return render (request,'hom/changepas.html',{'status':msg})

def teacher(request):
    msg = ""
    if request.method == 'POST':

        teachmail = request.POST['mail']
        teachpass = request.POST['pass']

        try :
            teacherlogin = Teacher.objects.get(email = teachmail,password = teachpass)
            request.session["teacher_id"] = teacherlogin.id
            return redirect("teacher:t_home")

        except:
            msg = 'invalid email or password'
    return render (request,'hom/t_login.html',{'status':msg,})
@auth_teacher
def viewstudent(request):
    students = student.objects.filter(teacher = request.session['teacher_id'])
    return render (request,'hom/view_student.html',{'student_list':students})

def log_out(request):
    del request.session['teacher_id']
    request.session.flush()
    return redirect('common:home')
