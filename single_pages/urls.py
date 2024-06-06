from django.urls import path, include
from . import views

# path에 들어온 url주소에 맞게 매핑 되어있는 vieW로 던진다.
urlpatterns = [
    # 기본 urls에서 넘어온 곳
    path("about_me/", views.aboutme),  # 여기까지 실제 주소는 127.0.0.1:8000/about_me 일때 동작
    path("", views.landing),  # 여기까지 실제 주소는 127.0.0.1:8000/ 이렇게 된다. views에서 index찾아가라
]
