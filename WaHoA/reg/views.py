from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import NewUser
from django.http import HttpResponse
#from .forms import DateForm

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
        birth = request.POST['birth']
        NewUser.objects.create_user(username=username,
        password=password, email=None, nickname=nickname,
        phone=phone, name=name, gender=gender, birth = birth)

        #if form.is_valid():
            # form.save()
            # username=form.cleaned_data['username']
            # password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/user/')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration/register.html',context)

@xframe_options_sameorigin
def content(request):
    return render(request,"content.html")

def registerValidate(request):
    try:
        NewUser.objects.get(username=request.POST['username'])
    except:
        return HttpResponse("Successful Register")
    else:
        return HttpResponse("Already registered")
