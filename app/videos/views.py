# from django.shortcuts import render
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
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            video = serializer.save()
            serializer = VideoSerializer(video)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)