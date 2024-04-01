from django.db import models
from common.models import CommonModel

# Create your models here.
# 제목, 내용, 작성자
# Feed와 User의 관계
# User : Feed = 1:N
class Feed(CommonModel):
    title = models.CharField(max_length = 30)
    content = models.CharField(max_length = 120)
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)