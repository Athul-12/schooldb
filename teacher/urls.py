from django.urls import path
from . import views
app_name = 'teacher'

urlpatterns = [
    path('home/',views.home, name='t_home'),
    path('profilr/',views.profil, name='t_prof'),
    path('addstu/',views.addstudent, name='addS'),
    path('viewS/',views.viewstudent, name='Sview'),
    path('changepass/',views.chnge, name='pass'),
    path('teacher',views.teacher, name='teacher'),
    path('logout/',views.log_out, name='logout')
]