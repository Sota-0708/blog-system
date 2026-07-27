# blog-post Specification

## Purpose
TBD - created by archiving change add-blogpost-model. Update Purpose after archive.
## Requirements
### Requirement: Blog post persistence
The system SHALL store blog posts with a title, content, creation timestamp, and a reference to the author who wrote them.

#### Scenario: Creating a blog post
- **WHEN** a blog post is created with a title, content, and author
- **THEN** the system persists the post with an automatically recorded creation timestamp

### Requirement: Blog post authorship
Each blog post SHALL be linked to exactly one author, referencing Django's built-in user model (`settings.AUTH_USER_MODEL`).

#### Scenario: Deleting an author removes their posts
- **WHEN** a user who has authored blog posts is deleted
- **THEN** all blog posts authored by that user SHALL also be deleted

#### Scenario: Accessing an author's posts
- **WHEN** retrieving a user's `posts` related manager
- **THEN** the system SHALL return all blog posts authored by that user

### Requirement: Default post ordering
The system SHALL order blog posts by creation date, most recent first, by default.

#### Scenario: Listing posts without explicit ordering
- **WHEN** blog posts are queried without an explicit `order_by`
- **THEN** the most recently created post SHALL appear first

### Requirement: Human-readable post representation
The system SHALL provide a human-readable string representation of a blog post for use in the Django admin interface.

#### Scenario: Viewing a post in the admin list
- **WHEN** a blog post is displayed as a string
- **THEN** the string SHALL include the post title and the author's username

