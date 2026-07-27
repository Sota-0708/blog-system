## Context

The Blog System project's overview describes a `User` entity with its own username/password fields. Django ships with a built-in, battle-tested `auth.User` model that already provides authentication, password hashing, and admin integration. Reimplementing a custom User model at this early stage would add unnecessary complexity for a "hello, world" level Django project.

## Goals / Non-Goals

**Goals:**
- Provide a working `BlogPost` model that supports the core reading/browsing workflows described in the project overview (newest-first listing, author filtering)
- Keep the authentication/user layer swappable for the future without requiring a model rewrite

**Non-Goals:**
- Implementing a custom `User` model (username uniqueness, custom fields) — deferred to a future change if needed
- Implementing views, URLs, or templates — covered by later exercises
- Implementing search or date-based filtering logic — covered by later exercises

## Decisions

**Decision: Use Django's built-in `auth.User` instead of a custom User model**
- Rationale: Django's built-in User already provides unique usernames, hashed passwords, and admin/login integration out of the box, satisfying the project overview's registration requirements without extra code.
- Alternative considered: A custom `User` model matching the overview's exact field list (`userID`, `username`, `password`, `created_date`). Rejected for now because it duplicates functionality Django already provides and adds migration complexity for authentication.

**Decision: Reference the author via `settings.AUTH_USER_MODEL` instead of importing `User` directly**
- Rationale: Importing `django.contrib.auth.models.User` directly hardcodes a dependency on the default user model. If the project later switches to a custom user model, all direct imports break. Using `settings.AUTH_USER_MODEL` (as Django's own migration framework already does via `swappable_dependency`) keeps the model consistent with Django best practice and future-proof.
- Alternative considered: Direct `from django.contrib.auth.models import User` import. Rejected after code review feedback, since it conflicts with the swappable reference already used in the generated migration.

**Decision: Default ordering via `Meta.ordering = ["-created_date"]`**
- Rationale: The project overview's primary workflow is "view all posts sorted by date, most recent first." Setting this at the model level means every default queryset already satisfies that requirement without repeating `.order_by()` in every view.

## Risks / Trade-offs

- [Risk] Using Django's built-in User means the `password` field is not stored as described in the overview (managed by Django's auth system instead) → Mitigation: this is intentional and safer; the overview's data model is treated as a functional description, not a literal schema.
- [Risk] `created_date` uses `auto_now_add`, so ordering ties could occur if two posts are created within the same second in a low-precision database → Mitigation: acceptable for the current development/testing scope (SQLite); revisit if the project moves to a production database with looser timestamp precision.
