from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import RegisterForm, BlogPostForm, SearchForm


def post_list(request):
    """Show blog posts, newest first, optionally filtered by search query."""
    form = SearchForm(request.GET)
    posts = BlogPost.objects.all()
    if form.is_valid() and form.cleaned_data["q"]:
        posts = posts.filter(title__icontains=form.cleaned_data["q"])
    return render(request, "blog/post_list.html", {"posts": posts, "form": form})


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_create(request):
    """Show a form to create a post, and process submission (login required)."""
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
    else:
        form = BlogPostForm()
    return render(request, "blog/post_form.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("post_list")
        return render(request, "blog/login.html", {"error": "Invalid credentials"})
    return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return redirect("post_list")