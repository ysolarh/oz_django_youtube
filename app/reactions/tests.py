# import pdb

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from videos.models import Video

from .models import Reaction


class ReactionAPITestCase(APITestCase):
    # 테스트 코드 실행 전에 필요한 더미 데이터 생성
    def setUp(self):
        self.user = User.objects.create_user(email='dkdk@gmail.com', password='12345asdf')
        self.video = Video.objects.create(
            title='test video',
            link='http://test.com',
            user=User.objects.get()
        )

        self.client.login(email='dkdk@gmail.com', password='12345asdf')

    # [POST] - 좋아요, 싫어요 생성 및 업데이트
    def test_reaction_detail_post(self):
        url = reverse('video-reaction', kwargs={'video_id': self.video.id})
        data = {
            'reaction': Reaction.LIKE
        }

        res = self.client.post(url, data)

        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reaction.objects.count(), 1)
        self.assertEqual(Reaction.objects.get().reaction, Reaction.LIKE)

    # [DELETE] - 좋아요, 싫어요 삭제
    def test_reaction_detail_delete(self):
        pass
