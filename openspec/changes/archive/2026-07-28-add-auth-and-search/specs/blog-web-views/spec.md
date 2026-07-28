## MODIFIED Requirements

### Requirement: Post creation page
The system SHALL provide a page at `GET /posts/new/` that renders a form for creating a new post, and SHALL accept `POST /posts/new/` with `title` and `content` fields to create the post. This page SHALL require the user to be logged in, and the post's author SHALL be the currently logged-in user.

#### Scenario: Viewing the creation form
- **WHEN** a logged-in user requests `GET /posts/new/`
- **THEN** the system SHALL respond with HTTP 200 and render a form containing title and content fields

#### Scenario: Submitting a new post
- **WHEN** a logged-in user submits `POST /posts/new/` with a non-empty `title` and `content`
- **THEN** the system SHALL create a new `BlogPost` authored by the logged-in user and redirect to the post list page

#### Scenario: Submitting without any users in the system
- **WHEN** a logged-in user submits `POST /posts/new/` and the system otherwise has no way to resolve an author
- **THEN** the system SHALL NOT create a post

#### Scenario: Viewing the creation form while logged out
- **WHEN** a logged-out user requests `GET /posts/new/`
- **THEN** the system SHALL redirect to the login page

#### Scenario: Submitting an invalid new post
- **WHEN** a logged-in user submits `POST /posts/new/` with an empty `title`
- **THEN** the system SHALL redisplay the form with a validation error and SHALL NOT create a post
