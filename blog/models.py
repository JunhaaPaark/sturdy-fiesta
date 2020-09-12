from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)  # ForeignKey는 many-to-one relationship을 정의하기 위해 사용된다.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 반드시 정의해주어야 하는 메소드. (모델 인스턴스의 이름 표시)
    def __str__(self):
        return self.title
