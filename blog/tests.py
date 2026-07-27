from django.test import TestCase
from django.contrib.auth.models import User
from .models import BlogPost


class BlogPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.post = BlogPost.objects.create(
            title="My first post",
            content="Hello, world!",
            author=self.user,
        )

    def test_str_representation(self):
        self.assertEqual(str(self.post), "My first post (testuser)")

    def test_post_is_linked_to_author(self):
        self.assertEqual(self.post.author.username, "testuser")

    def test_posts_ordered_by_newest_first(self):
        second_post = BlogPost.objects.create(
            title="Second post",
            content="Another post",
            author=self.user,
        )
        posts = list(BlogPost.objects.all())
        self.assertEqual(posts[0], second_post)  # 新しい方が先頭
        
    def test_related_name(self):
        self.assertEqual(self.user.posts.count(), 1)
        self.assertEqual(self.user.posts.first(), self.post)

    def test_delete_user_deletes_posts(self):
        self.user.delete()
        self.assertEqual(BlogPost.objects.count(), 0)