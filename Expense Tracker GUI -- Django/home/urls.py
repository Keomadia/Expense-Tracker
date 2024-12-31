
from django.contrib import admin
from django.urls import path ,include , re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.views.static import serve

app_name = 'home'

urlpatterns = [
    path('', views.home,name='home'),
    path('add/', views.add_expense,name='add'),
    path('all/', views.all_expense,name='all'),
    path('add_category/', views.add_category,name='add_category'),
    path('del/<int:srno>', views.del_expense,name='del'),
]

