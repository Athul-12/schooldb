from django.urls import path
from . import views 

urlpatterns = [
    path('home/',views.home, name='s_home'),
    path('prof/',views.profile, name='s_prof'),
    path('pass/',views.pas, name='chngepas')
]