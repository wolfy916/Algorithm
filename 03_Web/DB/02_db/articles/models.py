from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# 외래 키 데이터 입력 시 다음과 같이 article 객체 자체를 넣는 것을 권장
# comment.article = article

# line 7, 18 : settings.AUTH_USER_MODEL의 반환 값은 'accounts.User'(문자열)이며, 모델 필드에서 User 모델을 참조할 때 사용
# get_user_model()의 경우, 반환 값은 User Object(객체)이며, model.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용