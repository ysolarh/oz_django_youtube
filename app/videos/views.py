# from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer


class VideoList(APIView):
    # permission 관련 추가
    def get(self, request):
        videos = Video.objects.all()
        # print('videos: ', videos)
        # 직렬화 (장고객체 -> JSON) => serializer
        serializer = VideoSerializer(videos, many=True)  # 쿼리셋이 2개 이상
        return Response(serializer.data)

    def post(self, request):
        try:
            user_data = request.data
            serializer = VideoSerializer(data=user_data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class VideoDetail(APIView):
    def get_object(self, pk):
        # return get_object_or_404(Video, pk=pk)
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk):
        video = self.get_object(pk)
        user_data = request.data

        try:
            serializer = VideoSerializer(video, data=user_data)
            serializer.is_valid()
            # serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)