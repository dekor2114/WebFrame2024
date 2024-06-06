from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Category  # db쓸라면 import 해줘야한다.
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# 기본적인 MTV구조를 가지는데 이것은 DB에서 모델이 가져오면 그것을 Template에서 찾아서 View가 던져준다.
# Create your views here.

#CreateView를 가져와서 쓰겠다.
#여기서 찾는 templates은 post_form.html을 찾는다. (자동적으로)
#LoginRequiredMixin 로그인 상태 체크
#UserPassesTestMixin 누군지 체크하는 기능
# request여기에 user라는 값에 어떤 사용자인지 비어있으면 로그인이 안된 상태이다.
            
class CreatePost(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    #여러개를 동시에 상속 가능. 
    model = Post
    fields = ['title', 'content', 'head_image', "file_upload", 'category']
    # template_name = 'lllll' ---> 내가 원하는 이름으로 지정할떄 사용.
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.user = current_user
            return super(CreatePost, self).form_valid(form)

def category_page(request, slug):
    if slug == 'nocategory':
        category = '미분류'
        post_list = Post.objects.filter(category = None)
    else:
        category = Category.objects.get(slug = slug)
        post_list = Post.objects.filter(category=category)
    return render(
        request,
        'blog/post_list.html',{
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )



'''
FBV(function 베이스 방식)
# views.index 가 날아오는 곳 index로 던지니깐 def(index)로 받아주면서 우리가 띄우고자하는 blog를 띄워준다.
def index(request):
    posts = Post.objects.all().order_by("-pk")  # 데이타베이스에서 가져오는 모든 내용을 posts에 넣는다.
    # = select * from Post
    return render(
        request,
        "blog/index.html",  # 기본 주소는 templates안에 있는걸 찾는다. 그니깐 여기서는 tmplate안에 있는 폴더인 blog안에 index를 찾아라
        {
            "posts": posts,  # 그안에 필요한 파라미터를 json형태로 넘겨준다. (변수명:내용)
        },
    )  # render() = 화면에 띄워라


def single_post_page(request, pk):  # 여기 pk는 urls에서 넘겨준 pk이다.
    po1 = Post.objects.get(pk=pk)
    # = select * from Post where pk = pk 특정한 하나만 db에서 가져와라
    return render(
        request,
        "blog/single_post.html",
        {
            "pone": po1,  # 우리가 html파일에 po1이라는 우리가 받은 pk값을 pone이라는 이름으로 넘겨줄거야
        },
    )'''

#클래스 기반의 설계
#views.PostList.as_view()가 넘어오는 곳 / 전체를 가져오는 역활
class PostList(ListView): #ListView를 상속 받는다.
    model = Post #우리가 만든 Post를 연결시켜준다.
    ordering = '-pk'
    # template_name = 'blog/index.html' 해서 바꿀 수 있다. 찾는 html파일을 원래는 기본적으로 찾는 파일이 따로 있다.
    #자동 템플릿이름도 post_list로 찾는다.
    #여기서 variable : post_list로 넘어간다.
    #내가 원하는걸로 바꿀 때는 context_object_name = 'ps' 로 하면 변수를 ps 로 넘어간다.


    #카테고리할 때 작업한 것 컨택스트를 넘기기 위해서 오버라이딩을 한 것
    def get_context_data(self, **kwargs):
        #상위 클래스 한번 불러서 super 그래서 context에 넣어주는 것
        context = super(PostList, self).get_context_data()
        # context['post_list'] = Post.objects.all().order_by('-pk')
        # categories을 만들고 그안에 집어 넣는다.
        context['categories'] = Category.objects.all()
        #카테고리가 지정되지 않은 것들을 가져오는 것 숫자를 집어 넣고
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

#views.PostDetail.as_view()가 넘어오는 곳
class PostDetail(DetailView):
    model = Post
    #여기서 variable : post 넘어간다.

    #원하는것을 넘기고 싶을때 이걸 오버라이딩해서 보내야한다.
    def get_context_data(self, **kwargs):
        #상위 클래스 한번 불러서 super 그래서 context에 넣어주는 것
        #나 자신을 한번 더 넘겨서 context에 저장
        context = super(PostDetail, self).get_context_data()
        # context['post'] = Post.objects.get(pk=pk)
        # categories을 만들고 그안에 집어 넣는다.
        context['categories'] = Category.objects.all()
        #카테고리가 지정되지 않은 것들을 가져오는 것 숫자를 집어 넣고
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    




