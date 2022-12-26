from django.urls import path
from .import views
app_name = 'student_api'

urlpatterns = [
    path('load',views.load_student,name='load'),
    path('add',views.add_student, name='add'),
    path('del/<int:s_id>',views.del_student,name='del'),
    path('update/<int:s_id>',views.update_student,name='update'),
    path('index',views.index, name='index'),
    path('signup',views.signup,name='signup')
]