from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:comment_pk>/comments/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    # 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk값이므로 이름을 구분하여 변수를 넘김 -> variable routing
]
