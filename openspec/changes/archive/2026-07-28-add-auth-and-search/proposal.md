## Why

The Blog System overview requires users to register with a unique username and password before writing posts, and to be able to search for posts by query. Up to this point, posts were attributed to a hard-coded user and there was no way to filter the post list, so proper authentication and search input handling are needed to satisfy Exercise 8's requirement to replace stub functionality with real user input.

## What Changes

- Added user registration via Django's `UserCreationForm` (enforces unique usernames)
- Added login and logout views using Django's built-in `authenticate`/`login`/`logout`
- `post_create` now requires login (`@login_required`) and uses `request.user` as the author instead of a hard-coded user
- Replaced manual POST field access in `post_create` with a `ModelForm` (`BlogPostForm`), adding title validation
- Added a `SearchForm` (GET) on the post list page to filter posts by title

## Capabilities

### New Capabilities
- `blog-auth`: User registration, login, and logout
- `blog-search`: Filtering the post list by a search query

### Modified Capabilities
- `blog-web-views`: The post creation flow now requires authentication and uses form-based validation instead of raw POST access

## Impact

- New file: `blog/forms.py` (RegisterForm, BlogPostForm, SearchForm)
- Modified: `blog/views.py` (post_create, register, login_view, logout_view, post_list)
- Modified: `blog/urls.py` (register, login, logout routes)
- New templates: `register.html`, `login.html`
- Modified: `post_list.html`, `post_form.html`
- Modified: `blog_system/settings.py` (LOGIN_URL)
