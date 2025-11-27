"""
Sample data population script for Django Portfolio
Run this script to populate your portfolio with sample data to see how it looks.
You can then edit this data through the admin panel.

Usage:
    python populate_sample_data.py
"""

import os
import django
from datetime import date

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from main.models import Project, Experience, Education, Skill, About


def populate_about():
    """Create/update About information"""
    about = About.get_solo()
    about.name = "Your Name Here"
    about.tagline = "Full Stack Developer | Python Enthusiast | Problem Solver"
    about.bio = """I'm a passionate developer who loves building elegant solutions to complex problems. 
    With expertise in Python, Django, and modern web technologies, I create applications that make a difference. 
    When I'm not coding, you can find me exploring new technologies or contributing to open-source projects."""
    about.email = "your.email@example.com"
    about.location = "Your City, Country"
    about.github_url = "https://github.com/yourusername"
    about.linkedin_url = "https://linkedin.com/in/yourusername"
    about.save()
    print("✓ Created About information")


def populate_projects():
    """Create sample projects"""
    projects_data = [
        {
            'title': 'Portfolio Website',
            'description': 'A modern, retro-inspired portfolio website built with Django. Features include project showcases, resume display, and an admin panel for easy content management. Fully responsive and optimized for all devices.',
            'technologies': 'Python, Django, HTML, CSS, JavaScript',
            'github_link': 'https://github.com/yourusername/portfolio',
            'demo_link': '',
            'is_featured': True,
            'order': 1,
            'date_created': date(2024, 11, 1),
        },
        {
            'title': 'Task Management API',
            'description': 'RESTful API for task management with user authentication, CRUD operations, and real-time updates. Implements JWT authentication and includes comprehensive API documentation.',
            'technologies': 'Django REST Framework, PostgreSQL, Redis, Celery',
            'github_link': 'https://github.com/yourusername/task-api',
            'demo_link': '',
            'is_featured': True,
            'order': 2,
            'date_created': date(2024, 9, 15),
        },
        {
            'title': 'Weather Dashboard',
            'description': 'Interactive weather dashboard that displays real-time weather data with beautiful visualizations. Features location-based forecasts and weather alerts.',
            'technologies': 'React, Python, Flask, OpenWeather API, Chart.js',
            'github_link': 'https://github.com/yourusername/weather-dashboard',
            'demo_link': '',
            'is_featured': True,
            'order': 3,
            'date_created': date(2024, 7, 20),
        },
        {
            'title': 'E-Commerce Platform',
            'description': 'Full-featured e-commerce platform with shopping cart, payment integration, and order management. Includes admin dashboard for inventory management.',
            'technologies': 'Django, Stripe API, PostgreSQL, Bootstrap',
            'github_link': 'https://github.com/yourusername/ecommerce',
            'demo_link': '',
            'is_featured': False,
            'order': 4,
            'date_created': date(2024, 5, 10),
        },
    ]
    
    for data in projects_data:
        project, created = Project.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        if created:
            print(f"✓ Created project: {project.title}")
        else:
            print(f"  Project already exists: {project.title}")


def populate_experience():
    """Create sample work experience"""
    experiences_data = [
        {
            'company': 'Tech Solutions Inc.',
            'position': 'Senior Software Developer',
            'start_date': date(2022, 1, 1),
            'end_date': None,  # Current position
            'description': 'Leading development of scalable web applications using Django and React. Collaborating with cross-functional teams to deliver high-quality software solutions.',
            'achievements': '''Reduced application load time by 40% through optimization
Mentored 5 junior developers and conducted code reviews
Implemented CI/CD pipeline improving deployment efficiency by 60%
Led migration of legacy systems to modern architecture''',
            'order': 1,
        },
        {
            'company': 'Digital Innovations Ltd.',
            'position': 'Full Stack Developer',
            'start_date': date(2020, 6, 1),
            'end_date': date(2021, 12, 31),
            'description': 'Developed and maintained multiple client-facing web applications. Worked with modern frameworks and implemented RESTful APIs.',
            'achievements': '''Built 10+ production-ready web applications
Improved API response time by 50%
Implemented automated testing increasing code coverage to 85%
Collaborated with design team to create responsive interfaces''',
            'order': 2,
        },
        {
            'company': 'StartUp Ventures',
            'position': 'Junior Developer',
            'start_date': date(2019, 1, 1),
            'end_date': date(2020, 5, 31),
            'description': 'Contributed to various projects focusing on backend development and database optimization. Learned best practices in agile development.',
            'achievements': '''Developed features for 5 different projects
Optimized database queries improving performance by 30%
Participated in daily stand-ups and sprint planning
Wrote comprehensive documentation for APIs''',
            'order': 3,
        },
    ]
    
    for data in experiences_data:
        experience, created = Experience.objects.get_or_create(
            company=data['company'],
            position=data['position'],
            defaults=data
        )
        if created:
            print(f"✓ Created experience: {experience.position} at {experience.company}")
        else:
            print(f"  Experience already exists: {experience.position} at {experience.company}")


def populate_education():
    """Create sample education"""
    education_data = [
        {
            'institution': 'University of Technology',
            'degree': 'Bachelor of Science',
            'field_of_study': 'Computer Science',
            'start_date': date(2015, 9, 1),
            'end_date': date(2019, 6, 30),
            'description': 'Focused on software engineering, algorithms, and data structures. Completed capstone project on machine learning applications.',
            'gpa': '3.8/4.0',
            'order': 1,
        },
        {
            'institution': 'Online Learning Platform',
            'degree': 'Professional Certificate',
            'field_of_study': 'Full Stack Web Development',
            'start_date': date(2020, 1, 1),
            'end_date': date(2020, 6, 30),
            'description': 'Intensive program covering modern web development technologies including React, Node.js, and cloud deployment.',
            'gpa': '',
            'order': 2,
        },
    ]
    
    for data in education_data:
        edu, created = Education.objects.get_or_create(
            institution=data['institution'],
            degree=data['degree'],
            field_of_study=data['field_of_study'],
            defaults=data
        )
        if created:
            print(f"✓ Created education: {edu.degree} - {edu.institution}")
        else:
            print(f"  Education already exists: {edu.degree} - {edu.institution}")


def populate_skills():
    """Create sample skills"""
    skills_data = [
        # Programming Languages
        {'name': 'Python', 'category': 'languages', 'proficiency': 4, 'order': 1},
        {'name': 'JavaScript', 'category': 'languages', 'proficiency': 3, 'order': 2},
        {'name': 'TypeScript', 'category': 'languages', 'proficiency': 3, 'order': 3},
        {'name': 'SQL', 'category': 'languages', 'proficiency': 3, 'order': 4},
        {'name': 'HTML/CSS', 'category': 'languages', 'proficiency': 4, 'order': 5},
        
        # Frameworks
        {'name': 'Django', 'category': 'frameworks', 'proficiency': 4, 'order': 1},
        {'name': 'React', 'category': 'frameworks', 'proficiency': 3, 'order': 2},
        {'name': 'Flask', 'category': 'frameworks', 'proficiency': 3, 'order': 3},
        {'name': 'FastAPI', 'category': 'frameworks', 'proficiency': 2, 'order': 4},
        
        # Databases
        {'name': 'PostgreSQL', 'category': 'databases', 'proficiency': 3, 'order': 1},
        {'name': 'MySQL', 'category': 'databases', 'proficiency': 3, 'order': 2},
        {'name': 'MongoDB', 'category': 'databases', 'proficiency': 2, 'order': 3},
        {'name': 'Redis', 'category': 'databases', 'proficiency': 2, 'order': 4},
        
        # Tools
        {'name': 'Git', 'category': 'tools', 'proficiency': 4, 'order': 1},
        {'name': 'Docker', 'category': 'tools', 'proficiency': 3, 'order': 2},
        {'name': 'Linux', 'category': 'tools', 'proficiency': 3, 'order': 3},
        {'name': 'AWS', 'category': 'tools', 'proficiency': 2, 'order': 4},
        {'name': 'CI/CD', 'category': 'tools', 'proficiency': 3, 'order': 5},
    ]
    
    for data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=data['name'],
            category=data['category'],
            defaults=data
        )
        if created:
            print(f"✓ Created skill: {skill.name}")
        else:
            print(f"  Skill already exists: {skill.name}")


def main():
    """Main function to populate all data"""
    print("\n" + "="*50)
    print("Populating Portfolio with Sample Data")
    print("="*50 + "\n")
    
    print("Creating About information...")
    populate_about()
    
    print("\nCreating Projects...")
    populate_projects()
    
    print("\nCreating Work Experience...")
    populate_experience()
    
    print("\nCreating Education...")
    populate_education()
    
    print("\nCreating Skills...")
    populate_skills()
    
    print("\n" + "="*50)
    print("✓ Sample data population complete!")
    print("="*50)
    print("\nNext steps:")
    print("1. Run the development server: python manage.py runserver")
    print("2. Visit: http://localhost:8000")
    print("3. Admin panel: http://localhost:8000/secret-admin/")
    print("   Username: admin")
    print("   Password: admin123")
    print("\n4. Edit the sample data through the admin panel")
    print("5. Replace with your actual information")
    print("="*50 + "\n")


if __name__ == '__main__':
    main()

