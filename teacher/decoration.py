from django.shortcuts import render,redirect

def auth_teacher(func):
    def wrap(request, *args, **wkargs):
        if 'teacher_id' in request.session:
            return func(request, *args, **wkargs)
        else:
            return redirect('teacher:teacher')
    return wrap