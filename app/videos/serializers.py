from rest_framework.serializers import ModelSerializer
from .models import Video
from users.serializers import UserSerializer

from comments.serializers import CommentSerializer

from reactions.serializers import ReactionSerializer


class VideoSerializer(ModelSerializer):
    # USER - VIDEO(FK)
    # COMMENT(FK) - VIDEO
    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    # 부모가 자녀를 찾기 위해 필요한 개념: Reverse Accessor => comment

    class Meta:
        model = Video
        fields = '__all__'  # Video 모델의 전체 필드
        depth = 1
