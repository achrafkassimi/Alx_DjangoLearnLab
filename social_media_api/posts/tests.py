from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from posts.models import Post, Comment

User = get_user_model()

class PostCommentTests(APITestCase):

    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Create a post for user1
        self.post = Post.objects.create(
            author=self.user1,
            title="Post 1",
            content="Content of Post 1"
        )

        # Create a comment for the post
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user1,
            content="This is a comment"
        )

        # API URLs
        self.posts_url = reverse('post-list')
        self.comments_url = reverse('comment-list')
        self.post_url = reverse('post-detail', kwargs={'pk': self.post.id})
        self.comment_url = reverse('comment-detail', kwargs={'pk': self.comment.id})

    def test_create_post(self):
        # Test creating a post
        self.client.login(username='user1', password='password123')
        data = {'title': 'Post 2', 'content': 'Content of Post 2'}
        response = self.client.post(self.posts_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_create_comment(self):
        # Test creating a comment on a post
        self.client.login(username='user2', password='password123')
        data = {'post': self.post.id, 'content': 'This is a comment from user2'}
        response = self.client.post(self.comments_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_update_post(self):
        # Test updating a post (only by the post's author)
        self.client.login(username='user1', password='password123')
        data = {'title': 'Updated Post 1', 'content': 'Updated content of Post 1'}
        response = self.client.put(self.post_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post 1')

    def test_update_comment(self):
        # Test updating a comment (only by the comment's author)
        self.client.login(username='user1', password='password123')
        data = {'content': 'Updated comment content'}
        response = self.client.put(self.comment_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated comment content')

    def test_delete_post(self):
        # Test deleting a post (only by the post's author)
        self.client.login(username='user1', password='password123')
        response = self.client.delete(self.post_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_delete_comment(self):
        # Test deleting a comment (only by the comment's author)
        self.client.login(username='user1', password='password123')
        response = self.client.delete(self.comment_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)

    def test_permission_denied_on_update_post(self):
        # Test permission denial if a user tries to update another user's post
        self.client.login(username='user2', password='password123')
        data = {'title': 'Updated Post 1', 'content': 'Updated content of Post 1'}
        response = self.client.put(self.post_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permission_denied_on_update_comment(self):
        # Test permission denial if a user tries to update another user's comment
        self.client.login(username='user2', password='password123')
        data = {'content': 'Updated comment content'}
        response = self.client.put(self.comment_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_posts_by_title(self):
        # Test filtering posts by title
        self.client.login(username='user1', password='password123')
        response = self.client.get(self.posts_url, {'search': 'Post 1'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_pagination_of_posts(self):
        # Test pagination of posts
        self.client.login(username='user1', password='password123')

        # Create additional posts
        for i in range(15):
            Post.objects.create(
                author=self.user1,
                title=f"Post {i+2}",
                content=f"Content of Post {i+2}"
            )

        response = self.client.get(self.posts_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)  # Check that only 10 posts are returned

    def test_create_post_without_login(self):
        # Test that an unauthenticated user cannot create a post
        data = {'title': 'Post 3', 'content': 'Content of Post 3'}
        response = self.client.post(self.posts_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_comment_without_login(self):
        # Test that an unauthenticated user cannot create a comment
        data = {'post': self.post.id, 'content': 'This is a comment'}
        response = self.client.post(self.comments_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
