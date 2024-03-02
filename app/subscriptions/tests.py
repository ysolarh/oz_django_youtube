import pdb

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

from .models import Subscription


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user@gmail.com', password='password123')
        self.user2 = User.objects.create_user(email='user2@gmail.com', password='password123')
        self.client.login(email='user@gmail.com', password='password123')


    # api/v1/subscriptions
    def test_sub_list_post(self):
        url = reverse('subs-list')
        data = {
            'subscriber': self.user1.pk,
            'subscribed_to': self.user2.pk
        }

        res = self.client.post(url, data)
        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)


    # api/v1/subscriptions/{user_id}
    def test_sub_detail_delete(self):
        subs = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        url = reverse('subs-detail', kwargs={'pk': subs.id})
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
