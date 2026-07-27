from django.urls import reverse
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


class BlogViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="viewtester", password="pass123")
        self.post = BlogPost.objects.create(
            title="View test post", content="Some content", author=self.user
        )

    def test_post_list_status_code(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    def test_post_list_shows_post_title(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, "View test post")

    def test_post_detail_status_code(self):
        response = self.client.get(reverse("post_detail", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_shows_post_content(self):
        response = self.client.get(reverse("post_detail", args=[self.post.id]))
        self.assertContains(response, "View test post")

    def test_post_create_get_shows_form(self):
        response = self.client.get(reverse("post_create"))
        self.assertContains(response, "<form")

    def test_post_create_post_saves_new_post(self):
        response = self.client.post(reverse("post_create"), {
            "title": "New post via form",
            "content": "Form content",
        })
        self.assertRedirects(response, reverse("post_list"))
        self.assertTrue(BlogPost.objects.filter(title="New post via form").exists())
