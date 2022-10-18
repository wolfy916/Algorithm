from django.urls import path
from . import views

app_name = 'users'

# /api/users/
urlpatterns = [
    path('users/', views.user_list, name='users'),
    path('users/<int:user_pk>', views.user_detail),
    path('users/<int:user_pk>/clubs', views.user_club),
]
