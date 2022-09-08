from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

# AbstractUser 

# AuthenticationForm
# SetPasswordForm
# PasswordChangeForm
# AdminPasswordChangeForm
# User를 참조하는 form이 아니라, Custom user model을 사용해도 오류가 안남

# UserCreationForm
# UserChangeForm 
# 두개는 Meta class에서 등록된 모델이 User(기본)이어서 반드시 커스텀을 해줘야함
