from django.db import models

# Create your models here.
#databbase작업함.=> table 작성 => Schema 작성
#소문자는 패키지, 클래스 명만 대문자 시작(대부분)
#migrationss
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.pk}]{self.title}"

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'