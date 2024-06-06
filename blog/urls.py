from django.urls import path, include
from . import views

# path에 들어온 url주소에 맞게 매핑 되어있는 vieW로 던진다.
urlpatterns = [
    path('create_post/', views.CreatePost.as_view()),
    path('category/<str:slug>/', views.category_page), # .../blog/category/프로그래밍/ CBV방식으로 해야한다.
    # 기본 urls에서 넘어온 곳
    path("<int:pk>/", views.PostDetail.as_view()),
    #path("<int:pk>/", views.single_post_page),  # 127.0.0.1:8000/blog/(숫자)
    path("", views.PostList.as_view()) #클래스를 연결시켜준다.
    #path("", views.index),  # 여기까지 실제 주소는 127.0.0.1:8000/blog/ 이렇게 된다.
]
