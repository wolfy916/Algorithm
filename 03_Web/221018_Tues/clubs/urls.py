from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'clubs'
urlpatterns = [
    path('clubs/', views.club_list, name='club_list'),
]
