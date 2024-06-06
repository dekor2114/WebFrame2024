from django.contrib import admin
from .models import Post, Category

# Register your models here.
# 관리자 기능

admin.site.register(Post)  # /admin사이트에 Post등록해라~

class CategoryAdmin(admin.ModelAdmin): #관리자 권한으로 뭘 하는 prepopulated_fields는 자동 완성 기능을 지원해준다.
    prepopulated_fields = {'slug' : ('name', )}

#위에서 만든 클래스까지 등록을해줘야한다
admin.site.register(Category, CategoryAdmin)
