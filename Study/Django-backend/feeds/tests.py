from rest_framework.test import APITestCase
from rest_framework import status
from django.urls    import reverse
from .models    import Feed
from users.models   import User

class feedAPITestCase(APITestCase):
    # 각 테스트 메서드가 실행되기 전에 호출
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

        self.feed1 = Feed.objects.create(user=self.user, title='Test Title 1')
        self.feed2 = Feed.objects.create(user=self.user, title='Test Title 2')

    def test_get_all_feeds(self):
        url = reverse('all_feeds')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_get_feed_detail(self):
        url = reverse('feed_detail')