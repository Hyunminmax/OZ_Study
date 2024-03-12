from django.db import models
from common.models  import CommonModel

# Create your models here.
# 게시글
# - title
# - content
# - author
class Board(CommonModel):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default = 0)
    reviews = models.PositiveIntegerField(default = 0)

    user = models.ForeignKey('users.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.title
        