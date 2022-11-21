from django.contrib import admin
from django.urls import path,include
from .views import home,login,regitser,admin_page,error

urlpatterns = [
    path('home/',home,name='home-page'),
    path('login/',login,name="login-page"),
    path('register/',regitser,name="register-page"),
    path('admin_page',admin_page,name="admin-page"),
    path('error/',error,name='error-page')
]