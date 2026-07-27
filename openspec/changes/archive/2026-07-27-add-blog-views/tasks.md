## 1. Views
- [x] 1.1 Implement `post_list` view (show all posts, newest first)
- [x] 1.2 Implement `post_detail` view (show a single post, 404 if missing)
- [x] 1.3 Implement `post_create` view (GET shows form, POST creates post)
- [x] 1.4 Guard `post_create` against missing users (HTTP 400 instead of crashing)

## 2. URLs
- [x] 2.1 Create `blog/urls.py` with post_list, post_detail, post_create routes
- [x] 2.2 Include `blog.urls` in the project's root `urls.py`

## 3. Templates
- [x] 3.1 Create `post_list.html`
- [x] 3.2 Create `post_detail.html`
- [x] 3.3 Create `post_form.html`
- [x] 3.4 Format dates and preserve line breaks in templates

## 4. Testing
- [x] 4.1 Test post_list returns 200 and shows post titles
- [x] 4.2 Test post_detail returns 200 and shows post content
- [x] 4.3 Test post_create GET shows the form
- [x] 4.4 Test post_create POST creates a post and redirects to post_list

## 5. Review and integration
- [x] 5.1 Open pull request against `main`
- [x] 5.2 Perform code review with an alternative AI model
- [x] 5.3 Apply review feedback (fix duplicate import, fix reverse import position, guard missing author, improve templates and tests)
- [x] 5.4 Merge pull request and close linked issue
