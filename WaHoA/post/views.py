from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.
#進入myartickl.html


def home(request):   #已登入的首頁
    gender =request.user.gender
    if gender=='男male':
        return render(request, 'home.html',{"headpicture":"/static/head_boy.jpg"}) 
    else:
        return render(request, 'home.html',{"headpicture":"/static/head_girl.jpg"}) 

def get_post(request):
    number = Post.objects.all()
    gender = request.user.gender
    headpicture=""
    if gender == "男male":
        headpicture="/static/head_boy.jpg"
    else:
        headpicture="/static/head_girl.jpg"
    return render(request, 'user/myarticle/myarticle_addtime.html', {'number':number,'headpicture':headpicture}) #我的發文

def get_favorite(request):
    return render(request, 'user/myfavorite/myfavorite.html') #我的收藏
    
@xframe_options_sameorigin
def add_comment_2(request):
    return render(request,'user/myarticle/add_comment_2.html')


