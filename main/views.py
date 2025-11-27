from django.shortcuts import render
from django.views.defaults import page_not_found, server_error
from .models import Project, Experience, Education, Skill, About, Certificate


def custom_404(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error page"""
    return render(request, '500.html', status=500)


def home(request):
    """Homepage with intro and featured projects"""
    about = About.get_solo()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    
    context = {
        'about': about,
        'featured_projects': featured_projects,
    }
    return render(request, 'home.html', context)


def projects(request):
    """Projects page with all projects and filtering"""
    all_projects = Project.objects.all()
    
    # Get filter parameter
    tech_filter = request.GET.get('tech', '')
    
    # Filter by technology if specified
    if tech_filter:
        all_projects = all_projects.filter(technologies__icontains=tech_filter)
    
    # Get all unique technologies for filter dropdown
    all_techs = set()
    for project in Project.objects.all():
        all_techs.update(project.get_tech_list())
    all_techs = sorted(all_techs)
    
    context = {
        'projects': all_projects,
        'all_techs': all_techs,
        'current_tech': tech_filter,
    }
    return render(request, 'projects.html', context)


def resume(request):
    """Resume page with experience, education, certificates, and skills"""
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certificates = Certificate.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in Skill.objects.all():
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    about = About.get_solo()
    
    context = {
        'experiences': experiences,
        'education': education,
        'certificates': certificates,
        'skills_by_category': skills_by_category,
        'about': about,
    }
    return render(request, 'resume.html', context)


def contact(request):
    """Contact page with contact information"""
    about = About.get_solo()
    
    context = {
        'about': about,
    }
    return render(request, 'contact.html', context)
