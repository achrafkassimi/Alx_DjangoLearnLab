# accounts/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='password')
        self.user2 = get_user_model().objects.create_user(username='user2', password='password')

    def test_follow_user(self):
        self.client.login(username='user1', password='password')
        response = self.client.post(f'/accounts/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unfollow_user(self):
        self.client.login(username='user1', password='password')
        self.client.post(f'/accounts/follow/{self.user2.id}/')  # Follow first
        response = self.client.post(f'/accounts/unfollow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
