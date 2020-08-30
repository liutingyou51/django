from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import NewUser

def index_beforelogin(request):
    #e=request.POST["username"]
    #j=NewUser.objects.get(pk=e)
    #articals=j.artical_set.all()
    return render(request,'user_example/index_beforelogin.html')#,{"artical":articals}

def index(request):
    return render(request,'user_example/index.html')

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
        return render(request,'user_example/index.html')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration/register.html',context)
    
def myarticle_addtime(request):
    return render(request,'article/myarticle_addtime.html')

def myarticle_collect(request):
    return render(request,'article/myarticle_collect.html')

@xframe_options_sameorigin
def content(request):
    return render(request,"user_example/content.html")

@xframe_options_sameorigin
def post_article_choose(request):
    return render(request,'user_example/post_article_choose.html')

@xframe_options_sameorigin
def post_article_write(request):
    return render(request,'user_example/post_article_write.html')


