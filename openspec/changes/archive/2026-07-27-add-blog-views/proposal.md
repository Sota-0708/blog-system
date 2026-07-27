## Why

The Blog System needs basic web pages so users can browse posts and create new ones through a browser, turning the project from a data model into a working web application, as required by Exercise 6.

## What Changes

- Added `post_list` view: shows all blog posts, newest first (relies on the `BlogPost` model's default ordering)
- Added `post_detail` view: shows a single blog post by ID
- Added `post_create` view: shows a form (GET) and processes submission (POST) to create a new post
- Author is temporarily hard-coded to the first existing user, since login/authentication is not implemented yet
- Added templates for the list, detail, and form pages
- Connected all views to URLs via `blog/urls.py`, included from the project's root `urls.py`
- Added view-level tests (status codes, rendered content, redirect behavior)

## Capabilities

### New Capabilities
- `blog-web-views`: HTTP views and URLs for browsing and creating blog posts

### Modified Capabilities
(none)

## Impact

- New file: `blog/views.py`
- New file: `blog/urls.py`
- Modified: `blog_system/urls.py` (includes `blog.urls`)
- New templates: `blog/templates/blog/post_list.html`, `post_detail.html`, `post_form.html`
- Modified: `blog/tests.py` (added `BlogViewsTest`)
- Depends on `blog-post` capability (the `BlogPost` model) from the `add-blogpost-model` change
