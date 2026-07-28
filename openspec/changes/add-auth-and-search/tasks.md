## 1. Forms
- [x] 1.1 Create `RegisterForm` (based on `UserCreationForm`)
- [x] 1.2 Create `BlogPostForm` (ModelForm with title validation)
- [x] 1.3 Create `SearchForm` (GET, optional query field)

## 2. Views
- [x] 2.1 Add `register` view (GET shows form, POST creates user and logs in)
- [x] 2.2 Add `login_view` (GET shows form, POST authenticates and logs in)
- [x] 2.3 Add `logout_view`
- [x] 2.4 Update `post_create` to require login and use `request.user` as author
- [x] 2.5 Update `post_create` to use `BlogPostForm` instead of raw POST access
- [x] 2.6 Update `post_list` to filter posts using `SearchForm`

## 3. URLs and settings
- [x] 3.1 Add `register/`, `login/`, `logout/` routes
- [x] 3.2 Set `LOGIN_URL` in settings

## 4. Templates
- [x] 4.1 Create `register.html`
- [x] 4.2 Create `login.html`
- [x] 4.3 Add search form and login/register/logout links to `post_list.html`
- [x] 4.4 Update `post_form.html` to render the ModelForm

## 5. Testing
- [x] 5.1 Test post_create requires login
- [x] 5.2 Test post_create uses logged-in user as author
- [x] 5.3 Test post_create rejects empty title
- [x] 5.4 Test registration creates a user and logs them in
- [x] 5.5 Test search filters posts by title

## 6. Review and integration
- [x] 6.1 Open pull request against `main`
- [x] 6.2 Perform code review with an alternative AI model
- [x] 6.3 Fix unreachable search filter code, stray shell text in template, duplicate nav link and docstrings
- [x] 6.4 Merge pull request and close linked issue
