from django.shortcuts import render
from .models import Post

# Create your views here.

#views.index로 접근하는 친구
def index(request):
    posts = Post.objects.all().order_by('-pk')
    #select *from posts -sql
    #select *from posts order by desc -sql 꺼꾸로 가져오기
    return render(
        request,
        'blog/index.html',
        {
            'pst':posts, #변수명 : 값(들)
        }
    )
#views.single_page
def single_page(request, pk):
    #select *from Post where pk=pk
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'p_one' : post,
        }

    )