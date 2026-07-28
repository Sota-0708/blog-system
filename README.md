# Blog System

A simple Django blog application built for the Web Engineering course.

## Features

- Browse blog posts (newest first)
- View individual posts
- Search posts by title (with live HTMX updates)
- User registration and login
- Create posts (login required)

## Local development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deployment

This project is configured for deployment on [Render](https://render.com) using Gunicorn as the application server and WhiteNoise for serving static files.

### Environment variables

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key | (generate a random string) |
| `DEBUG` | Set to `False` in production | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `myapp.onrender.com` |
| `DATABASE_URL` | Provided automatically by Render's PostgreSQL add-on | `postgres://...` |

### Deploying to Render

1. Push this repository to GitHub.
2. Create a new Web Service on Render, connecting it to this repository.
3. Set the build command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

4. Set the start command:

```bash
gunicorn blog_system.wsgi --log-file -
```

5. Add a PostgreSQL instance on Render (this automatically sets the `DATABASE_URL` environment variable).
6. Set the environment variables listed above (`SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`).
7. Deploy. Render will build and start the service automatically on every push to `main`.

### Static files

Static files (CSS, JS) are served via [WhiteNoise](https://whitenoise.readthedocs.io/), which serves compressed, cache-friendly static assets directly from the Django app without needing a separate web server.

### Running locally with production-like settings

```bash
export DEBUG=False
export ALLOWED_HOSTS=localhost,127.0.0.1
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn blog_system.wsgi --log-file -
```
