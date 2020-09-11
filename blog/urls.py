from django.urls import path
from . import views

# post_list라는 view를 root URL에 할당
# 빈 문자열에 매칭
urlpatterns = [
    path('', views.post_list, name='post_list')
]
