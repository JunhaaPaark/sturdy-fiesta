'''
view 함수
input:
        1) URLconf를 통한 웹 클라이언트의 요청
        2) 장고 model과의 CRUD interaction
output:
        1) template 렌더링을 통해 나온 .html 파일 (웹 클라이언트에 표시됨)
        2) 장고 model과의 CRUD interaction

'''

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
