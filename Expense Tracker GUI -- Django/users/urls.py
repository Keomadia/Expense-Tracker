
from django.contrib import admin
from django.urls import path ,include , re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.views.static import serve

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]

