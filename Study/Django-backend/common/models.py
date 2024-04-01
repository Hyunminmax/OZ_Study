from django.db import models

# Create your models here.
class CommonModel(models.Model):
    # auto_now_add: 현재 데이터 생성 시간을 기준으로 생성, 이후 수정 X
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 생성되는 시간 기준으로 생성. 이후 업데이트시에서 수정 O
    updated_at = models.DateTimeField(auto_now=True)
    


    class Meta:
        abstract = True
