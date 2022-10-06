from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user',)

# 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        # 댓글 작성 시 누가 작성했는지, 어떤 게시글에 작성할 것인지
        # 사용자의 입력으로 받는 것이 아니라 view 함수 내에서 별도 처리 및 저장해야함
        exclude = ('article', 'user',)
