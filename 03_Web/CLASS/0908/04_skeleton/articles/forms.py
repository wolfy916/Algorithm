from django import forms
from .models import Article

# 상속 받을때는 첫 글자가 대문자여야함(첫 글자가 대문자라는 건 Class를 의미함)
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) # form에는 TextField가 없음!

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please 내용 입력'
        }
    )
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',) # 특정 필드만 제외하고 쓰고 싶을 때   