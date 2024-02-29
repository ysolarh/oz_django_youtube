from rest_framework.serializers import ModelSerializer
from .models import Video
from users.serializers import UserSerializer

from comments.serializers import CommentSerializer


class VideoSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)  # USER - VIDEO(FK)
    comment_set = CommentSerializer(many=True)  # COMMENT(FK) - VIDEO
    # 부모가 자녀를 찾기 위해 필요한 개념: Reverse Accessor => comment

    class Meta:
        model = Video
        fields = '__all__'  # Video 모델의 전체 필드
        depth = 1
