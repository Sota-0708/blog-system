## 1. Model implementation
- [x] 1.1 Create `BlogPost` model with title, content, created_date, author fields
- [x] 1.2 Reference author via `settings.AUTH_USER_MODEL` instead of importing `User` directly
- [x] 1.3 Set `Meta.ordering = ["-created_date"]` for newest-first default ordering
- [x] 1.4 Implement `__str__()` for admin readability

## 2. Database
- [x] 2.1 Generate migration with `makemigrations`
- [x] 2.2 Apply migration with `migrate`
- [x] 2.3 Register `BlogPost` in `admin.py`

## 3. Testing
- [x] 3.1 Test `__str__()` output
- [x] 3.2 Test author linkage
- [x] 3.3 Test default ordering (newest first)
- [x] 3.4 Test `related_name` access via `user.posts`
- [x] 3.5 Test cascade delete (deleting a user deletes their posts)

## 4. Review and integration
- [x] 4.1 Open pull request against `main`
- [x] 4.2 Perform code review with an alternative AI model
- [x] 4.3 Apply review feedback (switch to `settings.AUTH_USER_MODEL`, add cascade/related_name tests)
- [x] 4.4 Merge pull request and close linked issue
