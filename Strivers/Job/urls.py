from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('add_job',views.add_job,name='add_job'),
    path('remove_job/',views.remove_job,name='remove_job'),
    path('job/',views.show_jobs,name='job'),
    path('contactus/',views.contactus,name='contactus'),
]

