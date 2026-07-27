## Why

The Blog System project needs a persistent way to store blog posts and link them to their authors, so that the app can display, filter, and sort posts as described in the project overview (newest-first listing, author filtering, date filtering).

## What Changes

- Added a `BlogPost` Django model with fields: `title`, `content`, `created_date`, `author`
- `author` is a ForeignKey to `settings.AUTH_USER_MODEL` (Django's built-in User), not a custom User model
- Implemented `__str__()` on `BlogPost` for readable admin display
- Set `Meta.ordering = ["-created_date"]` so posts are returned newest-first by default
- Added unit tests covering `__str__`, author linkage, ordering, `related_name` access, and cascade delete behavior

## Capabilities

### New Capabilities
- `blog-post`: Data model and persistence for blog posts, including authorship and default ordering

### Modified Capabilities
(none — this is the first capability introduced for this project)

## Impact

- New file: `blog/models.py` (BlogPost model)
- New file: `blog/migrations/0001_initial.py`
- New file: `blog/tests.py`
- New file: `blog/admin.py` (basic registration)
- Depends on Django's built-in `auth.User` model — no custom user model introduced
