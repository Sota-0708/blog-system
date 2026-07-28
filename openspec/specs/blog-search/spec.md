# blog-search Specification

## Purpose
TBD - created by archiving change add-auth-and-search. Update Purpose after archive.
## Requirements
### Requirement: Search posts by title
The system SHALL allow a user to filter the post list by a search query matched against post titles.

#### Scenario: Query matches some posts
- **WHEN** a user submits a search query that matches one or more post titles
- **THEN** the system SHALL display only the matching posts

#### Scenario: Empty query
- **WHEN** a user submits an empty search query
- **THEN** the system SHALL display all posts, unfiltered

