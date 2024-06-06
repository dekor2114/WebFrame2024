# 거의 DB
import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# database 작업 -> migration작업을 해줘야지 반영이 된다.
# (python manage.py makemigrations)해서 찾아 준 후에 python manage.py migrate해서 업데이트 해야함
# 항상 이렇게 변화가 생기면 make로 변화 확인후 migration해서 반영을 해줘야한다 그럼 파일에 001, 002 이렇게 계속 생긴다.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) #겹치면 안돼
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) #한글 지원 가능

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"
    
    class Meta: # admin 사이트에서 보이는 카테고리의 이름을 지정해 줄 수 있다.
        verbose_name_plural = 'Categories'


# 기본 데이타베이스 테이블을 상속받아서 post라는 테이블을 만들겠다.
class Post(models.Model):  # table 작업 : database스키마 작성
    # 필드명 = models.타입지정
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                                        # 미디어 데이터들을 저장할 (시작은 미디어root부터 기준) 경로 설정
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank= True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank= True)

    #user, category와 연결해 주는 외래키를 설정하는 곳
    #1대 다의 관계 on_delete하면 지울 때 연관관계가 어떻게 할지 지정
    #1ㄷ1은 별로도 테이블을 굳이 나눌 필요가 없다.
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True ,on_delete=models.SET_NULL)

    # 화면에 어떻게 보일까 str함수를 사용해서 정해준다.
    def __str__(self):
        return f"[{self.created_at}] {self.title} :: {self.user}"  # f는 편수도 출력가능 pk는 프라이머리 키

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"
    
    def get_file_name(self): #파일이름만 띄우게하는 함수 생성
        return os.path.basename(self.file_upload.name)
    

