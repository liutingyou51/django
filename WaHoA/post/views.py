from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
#進入myartickl.html

@xframe_options_sameorigin
def home(request):   #已登入的首頁
    gender =request.user.gender
    if gender=='男male':
        return render(request, 'home.html',{"headpicture":"/static/head_boy.jpg"})
    else:
        return render(request, 'home.html',{"headpicture":"/static/head_girl.jpg"}) 
    #home.html用url叫圖片

def get_post(request):
    number = Post.objects.all()
    gender = request.user.gender
    headpicture=""
    if gender == "男male":
        headpicture="/static/head_boy.jpg"
    else:
        headpicture="/static/head_girl.jpg"
    return render(request, 'user/myarticle/myarticle_addtime.html', {'number':number,'headpicture':headpicture}) #我的發文
    #myarticle_add.html用url叫圖片
def get_favorite(request):
    gender = request.user.gender
    headpicture=""
    if gender == "男male":
        headpicture="/static/head_boy.jpg"
    else:
        headpicture="/static/head_girl.jpg"
    return render(request, 'user/myfavorite/myfavorite.html', {'headpicture':headpicture})
    #用url叫圖片
    
@xframe_options_sameorigin
def post_article_choose(request):
    if request.method == 'POST': 
        title = request.POST['title'] 
        content = request.POST['content']
        pub_date = timezone.now()
        Newpost = Post.objects.create(title = title, content = content, pub_date=pub_date)
        Newpost.save()
    return render(request,'post_article_choose.html')

@xframe_options_sameorigin
def post_article_write(request):
    return render(request,'post_article_write.html')  

@xframe_options_sameorigin
def create_post(request):
    return HttpResponse('test.html')

@xframe_options_sameorigin
def add_comment_2(request):
    gender =request.user.gender
    if gender=='男male':
        return render(request,'user/myarticle/add_comment_2.html',{"headpicture":"/head_boy.jpg"})
    else:
        return render(request,'user/myarticle/add_comment_2.html',{"headpicture":"/head_girl.jpg"})
        #用url叫會被擋，改用static
    

@xframe_options_sameorigin
def test(request):
    print(request.POST)
    if request.method =='POST':
        print("YES")
        comment = request.POST['comment_content']
        pub_date = timezone.now()
        Newcomment = Comment.objects.create(comment_content = comment, comment_datetime=pub_date)
        Newcomment.save()
        print("Success")
    else:
        print("fail")
    return  render(request,'user/myarticle/add_comment_2.html')