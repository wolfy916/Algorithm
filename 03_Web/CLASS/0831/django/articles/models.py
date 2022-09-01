from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 255자
    content = models.TextField() # 2의 31승 -1..?
    created_at = models.DateTimeField(auto_now_add=True) # 최초 생성 일자(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # 최종 수정 일자(auto_now=True)
    
