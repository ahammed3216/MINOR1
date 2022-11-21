from django.shortcuts import redirect, render
from .forms import LoginForm,RegisterForm, User
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model,authenticate
from .models import AdminModel
from django.core.mail import send_mail
user=get_user_model()
# Create your views here.


def home(request):
    return render (request,"home-page.html")

def admin_page(request):
    return render(request,'admin.html')

def login(request):
    form=LoginForm()
    return render(request,"login_page.html",{'form':form})

def error(request):
    return render(request,'error.html')

def regitser(request):

    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password_one=form.cleaned_data.get('password_one')
        password_two=form.cleaned_data.get('password_two')
        user.objects.create(username=username,email=email,password=password_one)

        send_mail((
            'Login',
                    'Your account has been registered sucessfully.your login credentials are username:'+username +'password:'+password_1,

                    'ayyarilnavad@gmail.com',
                    [email]
                    )
        )
        return redirect('/home')

    return render(request,"register.html",{'form':form})


def login(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get('email')
        password_one=form.cleaned_data.get('password')   
        user=User.objects.get(email=email)
        username=user.username
        user=authenticate(username=username,password=password_one)
 
        if user:
            print(user)
            auth_login(request,user)
            
            admin_user=AdminModel.objects.get(username=username)
            print(admin_user)
            if admin_user:
                return redirect('/admin_page')
            return redirect('/home')
        return redirect('')
        
    return render(request,'login_page.html',{'form':form})
        
