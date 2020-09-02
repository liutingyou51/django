from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone
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
    gender = request.user.gender
    headpicture=""
    if gender == "男male":
        headpicture="/static/head_boy.jpg"
    else:
        headpicture="/static/head_girl.jpg"
    return render(request, 'user/myfavorite/myfavorite.html', {'headpicture':headpicture})
    
@xframe_options_sameorigin
def post_article_choose(request):
    if request.method == 'POST': #是get不是post
        title = request.POST['title'] #沒找到
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
    if request.method == 'POST':
        kind = request.POST['kind']
        print(Post.objects.latest('pub_date'))
        Post.objects.latest('pub_date').update(kind=kind)
        print("successful updated")
    else:
        print("fail!")
    return render(request, 'test.html')

@xframe_options_sameorigin
def add_comment_2(request):
    request.method=='POST'
    return render(request,'user/myarticle/add_comment_2.html')


