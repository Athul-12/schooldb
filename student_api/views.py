from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import student1
from .serializer import StudentSerializer
from django.http import JsonResponse



# Create your views here.
@api_view(['GET'])
def load_student(request):
    students = student1.objects.all() 
    serialized_data = StudentSerializer(students, many = True)
    return JsonResponse(serialized_data.data, safe=False)

@api_view(['POST'])
def add_student(request):
    serialized_data = StudentSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'messege' : 'data insert success'})

    else:
        print('form not valid')
        return JsonResponse({'messege' : 'error'})

@api_view(['DELETE'])
def del_student(request,s_id):
    student = student1.objects.get(id = s_id)
    student.delete()
    return JsonResponse({'messege':"deleted successfully"})

@api_view(['PUT'])
def update_student(request,s_id):
    student = student1.objects.get(id=s_id)
    serialized_data = StudentSerializer(student,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'messege':'update successfully'})
    else:
        return JsonResponse({'messege':'errorr'})
@api_view(['GET'])
def index(request):
    messege = "congratulation, you have create an API"
    return Response(messege)

def signup(request):
    return render (request,'stu/signup.html')