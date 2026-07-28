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
        self.client.login(username="viewtester", password="pass123")

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

class BlogFormsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="formtester", password="pass123")

    def test_post_create_requires_login(self):
        response = self.client.get(reverse("post_create"))
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_post_create_uses_logged_in_user_as_author(self):
        self.client.login(username="formtester", password="pass123")
        response = self.client.post(reverse("post_create"), {
            "title": "Logged in post",
            "content": "Some content",
        })
        self.assertRedirects(response, reverse("post_list"))
        post = BlogPost.objects.get(title="Logged in post")
        self.assertEqual(post.author, self.user)

    def test_post_create_rejects_empty_title(self):
        self.client.login(username="formtester", password="pass123")
        response = self.client.post(reverse("post_create"), {
            "title": "",
            "content": "Some content",
        })
        self.assertEqual(response.status_code, 200)  # re-renders form with errors
        self.assertFalse(BlogPost.objects.filter(content="Some content").exists())

    def test_register_creates_user_and_logs_in(self):
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "password1": "SuperSecret123",
            "password2": "SuperSecret123",
        })
        self.assertRedirects(response, reverse("post_list"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_search_filters_posts_by_title(self):
        BlogPost.objects.create(title="Django tips", content="x", author=self.user)
        BlogPost.objects.create(title="Cooking recipes", content="y", author=self.user)
        response = self.client.get(reverse("post_list"), {"q": "django"})
        self.assertContains(response, "Django tips")
        self.assertNotContains(response, "Cooking recipes")

class HtmxSearchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="htmxtester", password="pass123")
        BlogPost.objects.create(title="Django tips", content="x", author=self.user)
        BlogPost.objects.create(title="Cooking recipes", content="y", author=self.user)

    def test_post_search_returns_partial_html(self):
        response = self.client.get(reverse("post_search"), {"q": "django"})
        self.assertContains(response, "Django tips")
        self.assertNotContains(response, "Cooking recipes")
        self.assertNotContains(response, "<html")  # partial only, not a full page

    def test_post_search_empty_query_returns_all(self):
        response = self.client.get(reverse("post_search"), {"q": ""})
        self.assertContains(response, "Django tips")
        self.assertContains(response, "Cooking recipes")