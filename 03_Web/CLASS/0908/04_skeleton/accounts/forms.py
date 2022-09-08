from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',) # 회원 가입시 email도 받고 싶을때..


class CustomUserChangeForm(UserChangeForm):
    # password = None # 비밀번호 보기 싫을 때

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)




# UserCreationForm
# UserChangeForm 
# 두개는 Meta class에서 등록된 모델이 User(기본)이어서 반드시 커스텀을 해줘야함