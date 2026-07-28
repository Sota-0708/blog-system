from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("search/", views.post_search, name="post_search"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("posts/new/", views.post_create, name="post_create"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]