## ADDED Requirements

### Requirement: User registration
The system SHALL allow a visitor to register a new account with a unique username and a password, and SHALL reject registration if the username is already taken.

#### Scenario: Successful registration
- **WHEN** a visitor submits the registration form with a unique username and matching passwords
- **THEN** the system SHALL create the account, log the user in, and redirect to the post list

#### Scenario: Duplicate username
- **WHEN** a visitor submits the registration form with a username that already exists
- **THEN** the system SHALL reject the submission and redisplay the form with a validation error

### Requirement: User login
The system SHALL allow a registered user to log in with their username and password.

#### Scenario: Successful login
- **WHEN** a user submits valid credentials on the login form
- **THEN** the system SHALL log the user in and redirect to the post list

#### Scenario: Invalid credentials
- **WHEN** a user submits an incorrect username or password
- **THEN** the system SHALL display an error message and SHALL NOT log the user in

### Requirement: User logout
The system SHALL allow a logged-in user to log out.

#### Scenario: Logging out
- **WHEN** a logged-in user requests the logout URL
- **THEN** the system SHALL end their session and redirect to the post list
