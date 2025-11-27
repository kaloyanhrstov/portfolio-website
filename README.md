# Django Portfolio Website

A modern portfolio website with retro aesthetic built with Django, showcasing projects, resume information, and more.

## Features

- **Admin Panel**: Easy content management through Django admin
- **Project Showcase**: Display your projects with descriptions, tech stacks, and GitHub links
- **Resume Section**: Experience, education, and skills
- **Modern + Retro Design**: Clean UI with retro aesthetic vibes
- **Secure**: Environment variables, HTTPS, and security best practices
- **Free Hosting**: Deployable to PythonAnywhere for free

## Tech Stack

- Django 5.1.3
- Python 3.10+
- SQLite Database
- HTML5/CSS3/JavaScript
- python-decouple for environment variables
- Pillow for image handling

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── portfolio_project/          # Main project folder
│   ├── settings.py            # Settings with env vars
│   ├── urls.py
│   └── wsgi.py
├── main/                      # Main app
│   ├── models.py              # Content models
│   ├── admin.py               # Customized admin
│   ├── views.py               # Page views
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── projects.html
│   │   ├── resume.html
│   │   └── contact.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
└── db.sqlite3
```
## Security Features

- Environment variables for sensitive data
- HTTPS enforcement in production
- Secure admin URL
- CSRF protection
- Security headers middleware
- Secure cookie settings in production
