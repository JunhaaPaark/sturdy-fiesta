from django.urls import path
from . import views

# post_list라는 view를 root URL에 할당
# root URL, 즉 junhaapaark.pythonanywhere.com은 빈 문자열에 매칭된다.\
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
