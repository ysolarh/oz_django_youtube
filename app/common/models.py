from django.db import models


class CommonModel(models.Model):
    # 데이터가 생성된 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 데이터가 업데이트된 시간 => 업데이트된 시간으로 최신화
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # DB 테이블에 추가안함
