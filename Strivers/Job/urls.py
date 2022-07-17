from django.urls import path
from . import views

# urlpatterns = [
#     path('',views.index,name='index'),
#     path('login',views.user_login,name='login'),
#     path('register',views.register,name='register'),
#     path('logout',views.user_logout,name='logout'),
# ]



urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('add_job/',views.add_job,name='add_job/'),
    path('job/',views.show_jobs,name='job/'),

    # path('add_jobs',views.add_jobs,name='add_jobs'),
    # path('jobs',views.show_jobs,name='jobs'),
    # path('mail',views.mail,name='mail')
]