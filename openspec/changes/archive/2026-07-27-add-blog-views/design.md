## Context

The `BlogPost` model already exists (from the `add-blogpost-model` change). This change adds the minimal web-facing layer (views, URLs, templates) needed to browse and create posts through a browser, as required by Exercise 6.

## Goals / Non-Goals

**Goals:**
- Provide working, navigable pages for listing, viewing, and creating posts
- Keep the implementation intentionally simple, matching Exercise 6's scope ("views do not need to be complete yet")

**Non-Goals:**
- Authentication/login (author is temporarily hard-coded to the first existing user)
- Form validation beyond what Django provides by default
- Styling/shared page layout (deferred to Exercise 7, which covers templates and sessions)

## Decisions

**Decision: Use function-based views instead of class-based views**
- Rationale: The project is small and the views are simple (list, detail, create). Function-based views keep the logic explicit and easy to follow for a project at this stage.
- Alternative considered: Django generic class-based views (`ListView`, `DetailView`, `CreateView`). Rejected for now to keep the implementation transparent while the project's conventions are still being established; may be revisited later.

**Decision: Hard-code the post author to the first existing user**
- Rationale: Login/authentication is out of scope for this exercise. Using `User.objects.first()` with an explicit guard (HTTP 400 if no users exist) keeps the view functional without pretending authentication is implemented.
- Alternative considered: Using `request.user`, which requires a working login system. Deferred until authentication is implemented.

## Risks / Trade-offs

- [Risk] All new posts are attributed to the same user regardless of who submits the form → Mitigation: acceptable for this exercise's scope; will be replaced by `request.user` once login is implemented.
- [Risk] No input validation on the creation form (e.g., empty title) → Mitigation: acceptable for this exercise's scope; a `ModelForm` with validation is planned as a follow-up change.
