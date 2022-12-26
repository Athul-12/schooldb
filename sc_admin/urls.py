from unicodedata import name
from django.urls import path
from . import views
app_name="sc_admin"
urlpatterns = [
    path('sc_home/',views.home,name='a_home'),
    path('add_teacher/',views.AddTeach, name='addteacher'),
    path('view_student/',views.viewstudent, name='viewstudent'),
    path('viewteacher/',views.ViewTeach, name='viewteacher'),
    path('changpass/',views.ChngPas, name='changepas'),
    path('admin',views.adm, name='adm'),
    path('emailex',views.email_exist, name='emailex'),
    path('fnAngularTest', views.fnAngularTest)
]