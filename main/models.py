from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_link = models.URLField(max_length=500, blank=True)
    demo_link = models.URLField(max_length=500, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Display on homepage")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    date_created = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-date_created']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_tech_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class Experience(models.Model):
    """Model for work experience"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current position")
    description = models.TextField()
    achievements = models.TextField(blank=True, help_text="One achievement per line")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return f"{self.position} at {self.company}"

    @property
    def is_current(self):
        """Check if this is a current position"""
        return self.end_date is None

    def get_duration(self):
        """Return formatted duration string"""
        start = self.start_date.strftime('%b %Y')
        end = self.end_date.strftime('%b %Y') if self.end_date else 'Present'
        return f"{start} - {end}"

    def get_achievements_list(self):
        """Return achievements as a list"""
        return [ach.strip() for ach in self.achievements.split('\n') if ach.strip()]


class Education(models.Model):
    """Model for education"""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if currently studying")
    description = models.TextField(blank=True)
    gpa = models.CharField(max_length=50, blank=True, help_text="e.g., 3.8/4.0")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} - {self.institution}"

    def get_duration(self):
        """Return formatted duration string"""
        start = self.start_date.strftime('%Y')
        end = self.end_date.strftime('%Y') if self.end_date else 'Present'
        return f"{start} - {end}"


class Certificate(models.Model):
    """Model for professional certificates and course completions"""
    title = models.CharField(max_length=200, help_text="Certificate title or course name")
    issuing_organization = models.CharField(max_length=200, help_text="e.g., Coursera, Udemy, AWS, etc.")
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True, help_text="Leave blank if no expiry")
    credential_id = models.CharField(max_length=200, blank=True, help_text="Certificate ID or credential number")
    credential_url = models.URLField(max_length=500, blank=True, help_text="Link to verify certificate")
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True, help_text="Upload certificate image")
    description = models.TextField(blank=True, help_text="Additional details about the certificate")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-issue_date']
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"

    def get_date_display(self):
        """Return formatted date string"""
        issue = self.issue_date.strftime('%b %Y')
        if self.expiry_date:
            expiry = self.expiry_date.strftime('%b %Y')
            return f"{issue} - Expires {expiry}"
        return issue

    @property
    def is_expired(self):
        """Check if certificate is expired"""
        if self.expiry_date:
            from django.utils import timezone
            return self.expiry_date < timezone.now().date()
        return False


class Skill(models.Model):
    """Model for skills"""
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('tools', 'Tools & Technologies'),
        ('databases', 'Databases'),
        ('other', 'Other'),
    ]

    PROFICIENCY_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(
        choices=PROFICIENCY_CHOICES,
        default=2,
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    order = models.IntegerField(default=0, help_text="Display order within category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    def get_proficiency_percentage(self):
        """Return proficiency as a percentage"""
        return (self.proficiency / 4) * 100


class About(models.Model):
    """Model for about/contact information (Singleton)"""
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300, help_text="Short description/tagline")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(max_length=500, blank=True)
    linkedin_url = models.URLField(max_length=500, blank=True)
    twitter_url = models.URLField(max_length=500, blank=True)
    website_url = models.URLField(max_length=500, blank=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True, help_text="PDF resume file")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Ensure only one instance exists (Singleton pattern)"""
        if not self.pk and About.objects.exists():
            # If trying to create a new instance when one exists, update existing instead
            existing = About.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        """Get the singleton instance"""
        obj, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'name': 'Your Name',
                'tagline': 'Your tagline here',
                'bio': 'Your bio here',
                'email': 'your.email@example.com',
            }
        )
        return obj
