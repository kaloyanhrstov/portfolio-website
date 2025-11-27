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

## ⚠️ Security Notice - Before Public Deployment

**IMPORTANT**: This repository contains example data. Before deploying to production:

1. **Generate a new SECRET_KEY** (never use the default!)
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
2. **Change the admin password** from `admin123` to a strong password
3. **Create a `.env` file** (copy from `.env.example`) and set your environment variables
4. **Set `DEBUG=False`** in production
5. **Never commit** your `.env` file, `db.sqlite3`, or `media/` folder with personal data

See [DEPLOYMENT.md](DEPLOYMENT.md) for the complete security checklist.

## Quick Start

The project is already set up and ready to use! Here's what's been done:

✅ Virtual environment created and activated
✅ All dependencies installed
✅ Database migrations applied
✅ Admin user created (username: `admin`, password: `admin123`)
✅ Sample data populated
✅ Development server is running

### Access Your Portfolio

1. **View the website**: Open your browser and visit:
   - Homepage: http://localhost:8000
   - Projects: http://localhost:8000/projects/
   - Resume: http://localhost:8000/resume/
   - Contact: http://localhost:8000/contact/

2. **Admin Panel**: http://localhost:8000/secret-admin/
   - Username: `admin`
   - Password: `admin123`
   - **Important**: Change this password in production!

### Customize Your Portfolio

1. Log in to the admin panel
2. Update the "About Me" section with your information
3. Replace sample projects with your actual projects
4. Add your real work experience and education
5. Update skills to match your expertise
6. Upload your profile picture and project images

### If You Need to Start Fresh

If the server isn't running or you need to set up the project again:

```bash
# Navigate to project directory
cd /home/kandh/portfolio

# Activate virtual environment
source venv/bin/activate

# Run the development server
python manage.py runserver

# In a new terminal, you can populate sample data again
python populate_sample_data.py
```

## Local Development Setup (For New Clones)

If you're setting up this project on a new machine:

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment variables (Optional)

The project uses `python-decouple` with sensible defaults. For production, set:

```bash
export SECRET_KEY='your-secret-key-here'
export DEBUG='False'
export ALLOWED_HOSTS='your-domain.com'
```

To generate a new secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Populate sample data (optional)

```bash
python populate_sample_data.py
```

### 7. Run the development server

```bash
python manage.py runserver
```

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

## Deployment to PythonAnywhere

1. Create a free account at [PythonAnywhere](https://www.pythonanywhere.com)
2. Upload your code via Git or the file manager
3. Set up a virtual environment on PythonAnywhere
4. Configure the WSGI file
5. Set environment variables in the PythonAnywhere web app settings
6. Run migrations on the production database
7. Collect static files: `python manage.py collectstatic`
8. Create a superuser on production
9. Your site will be available at: `https://yourusername.pythonanywhere.com`

## Adding Content

1. Log in to the admin panel at `/secret-admin/`
2. Add your projects with descriptions and GitHub links
3. Fill in your experience, education, and skills
4. Update your about/contact information
5. Changes appear immediately on the site

## Security Features

- Environment variables for sensitive data
- HTTPS enforcement in production
- Secure admin URL
- CSRF protection
- Security headers middleware
- Secure cookie settings in production

## License

MIT License - feel free to use for your own portfolio!

