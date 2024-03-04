from rest_framework.status import ( \
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Reaction
from .serializers import ReactionSerializer
from videos.models import Video


class ReactionDetail(APIView):
    # 좋아요, 싫어요 생성 or 업데이트
    def post(self, request, video_id):
        user_data = request.data  # 유저가 서버로 보낸 데이터
        # serializer
        serializer = ReactionSerializer(data=user_data)

        # is_valid
        if serializer.is_valid():
            print('serializer.validated_data:', serializer.validated_data)  # {'reaction': 1}
            # 좋아요 클릭했는데 이미 기존 데이터가 존재 => UPDATE
            # 데이터 존재하지 않는다면 => CREATE
            reaction_obj, created = Reaction.objects.get_or_create(
                user=request.user,
                video=Video.objects.get(id=video_id),
                defaults={'reaction': serializer.validated_data['reaction']}
            )

            # created: boolean(True: 새로 생성, False: 기존 객체가 존재)
            if created:
                return Response(serializer.data, status=HTTP_201_CREATED)
            # 기존 데이터가 존재하는 경우 => UPDATE
            if not created:
                reaction_obj.reaction = serializer.validated_data['reaction']
                reaction_obj.save()
                return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def delete(self):
        pass
