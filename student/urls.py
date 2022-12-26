from django.urls import path
from . import views 
app_name = 'student'

urlpatterns = [
    path('home/',views.home, name='s_home'),
    path('prof/',views.profile, name='s_prof'),
    path('pass/',views.pas, name='chngepas'),
    path('student',views.students, name='student'),
    path('logout',views.log_out, name='logout')
]