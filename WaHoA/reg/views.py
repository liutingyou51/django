from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import NewUser

def home_beforelogin(request):
    return render(request, 'home_beforelogin.html',)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        nickname = request.POST['nickname']
        phone = request.POST['phone']
        name = request.POST['name']
        gender = request.POST['gender']
        NewUser.objects.create_user(username=username,password=password,email=None,nickname=nickname,phone=phone,name=name,gender=gender)

        #if form.is_valid():
            # form.save()
            # username=form.cleaned_data['username']
            # password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        return render(request,'home.html')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration/register.html',context)