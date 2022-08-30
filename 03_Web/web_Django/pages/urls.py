from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('image/', views.image, name='image'),
    path("template_language/", views.template_language, name='template_language'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/<int:age>/', views.hello, name='hello'),
    path('ispal/<str:name>/', views.ispal, name='ispal'),
    path('lotto/', views.lotto, name='lotto'),
]