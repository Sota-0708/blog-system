## Context

Up to this point, `post_create` hard-coded the author to the first existing user, and there was no way for a real visitor to identify themselves or search the post list. This change introduces authentication and search, both required by the Blog System overview and Exercise 8.

## Goals / Non-Goals

**Goals:**
- Allow visitors to register and log in using Django's built-in authentication system
- Attribute new posts to the actual logged-in user
- Let users filter the post list by a search query

**Non-Goals:**
- Password reset / email verification flows
- Author or date filtering (covered by a separate future change, per the Blog System overview)
- Full-text search across post content (title-only for this iteration)

## Decisions

**Decision: Use Django's built-in authentication system (`UserCreationForm`, `authenticate`, `login`, `logout`) instead of a custom implementation**
- Rationale: Django's auth system already provides password hashing, session management, and username uniqueness validation, which matches the project's earlier decision to use `auth.User` instead of a custom User model.
- Alternative considered: Writing custom registration/login logic. Rejected as unnecessary duplication of well-tested framework functionality.

**Decision: Use `@login_required` to gate post creation, rather than a manual check inside the view**
- Rationale: `@login_required` is the standard Django idiom, automatically redirects anonymous users to the login page, and keeps the view body focused on its actual logic.
- Alternative considered: Manually checking `request.user.is_authenticated` inside `post_create`. Rejected as more verbose and easier to forget to update consistently.

**Decision: Search matches only the post title, using `icontains`**
- Rationale: Keeps the first search iteration simple and fast to implement, matching Exercise 8's scope of introducing basic user input handling.
- Alternative considered: Matching both title and content. Deferred to a future iteration to keep this change's scope focused.

## Risks / Trade-offs

- [Risk] Search is case-insensitive substring matching only, with no ranking or full-text search → Mitigation: acceptable for the current scale of the project; can be revisited if the dataset grows.
- [Risk] No rate limiting on login attempts → Mitigation: acceptable for a local development/course project; would need addressing before any real deployment.
