from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import BlogPost


def post_list(request):
    """Show all blog posts, newest first (uses model's default ordering)."""
    posts = BlogPost.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    """Show a single blog post."""
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


def post_create(request):
    """Show a form to create a post, and process submission."""
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        # TODO: replace with request.user once login is implemented
        author = User.objects.first()
        if author is None:
            return HttpResponse(
                "No users exist yet. Create a user via createsuperuser first.",
                status=400,
            )
        BlogPost.objects.create(title=title, content=content, author=author)
        return redirect("post_list")
    return render(request, "blog/post_form.html")
