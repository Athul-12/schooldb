import imp
from django.shortcuts import redirect,render



def auth_student(func):
    def wrap(request, *args, **wkargs):
        if 'student_id' in request.session:
            return func(request, *args, **wkargs)
        else:
            return redirect('student:student')
    return wrap