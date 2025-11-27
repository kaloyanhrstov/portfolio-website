from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Experience, Education, Skill, About, Certificate


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'is_featured', 'order', 'has_github', 'has_demo', 'image_preview']
    list_filter = ['is_featured', 'date_created']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['is_featured', 'order']
    ordering = ['order', '-date_created']
    date_hierarchy = 'date_created'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technologies', 'date_created')
        }),
        ('Links', {
            'fields': ('github_link', 'demo_link')
        }),
        ('Display Settings', {
            'fields': ('image', 'is_featured', 'order')
        }),
    )

    def has_github(self, obj):
        return bool(obj.github_link)
    has_github.boolean = True
    has_github.short_description = 'GitHub'

    def has_demo(self, obj):
        return bool(obj.demo_link)
    has_demo.boolean = True
    has_demo.short_description = 'Demo'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Image'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['company', 'start_date']
    search_fields = ['position', 'company', 'description', 'achievements']
    list_editable = ['order']
    ordering = ['order', '-start_date']
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Position Information', {
            'fields': ('company', 'position', 'start_date', 'end_date')
        }),
        ('Details', {
            'fields': ('description', 'achievements')
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )

    def is_current(self, obj):
        return obj.is_current
    is_current.boolean = True
    is_current.short_description = 'Current'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'field_of_study', 'institution', 'start_date', 'end_date', 'gpa', 'order']
    list_filter = ['institution', 'degree', 'start_date']
    search_fields = ['institution', 'degree', 'field_of_study', 'description']
    list_editable = ['order']
    ordering = ['order', '-start_date']
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Academic Information', {
            'fields': ('institution', 'degree', 'field_of_study', 'gpa')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Additional Details', {
            'fields': ('description',)
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuing_organization', 'issue_date', 'expiry_date', 'has_credential_id', 'has_image', 'order']
    list_filter = ['issuing_organization', 'issue_date']
    search_fields = ['title', 'issuing_organization', 'credential_id', 'description']
    list_editable = ['order']
    ordering = ['order', '-issue_date']
    date_hierarchy = 'issue_date'
    
    fieldsets = (
        ('Certificate Information', {
            'fields': ('title', 'issuing_organization', 'issue_date', 'expiry_date')
        }),
        ('Credentials', {
            'fields': ('credential_id', 'credential_url')
        }),
        ('Certificate Image', {
            'fields': ('certificate_image',)
        }),
        ('Additional Details', {
            'fields': ('description',)
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )

    def has_credential_id(self, obj):
        return bool(obj.credential_id)
    has_credential_id.boolean = True
    has_credential_id.short_description = 'Has ID'

    def has_image(self, obj):
        return bool(obj.certificate_image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'proficiency_bar', 'order']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    list_editable = ['category', 'proficiency', 'order']
    ordering = ['category', 'order', 'name']
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency')
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )

    def proficiency_bar(self, obj):
        percentage = obj.get_proficiency_percentage()
        color = '#00ff00' if percentage >= 75 else '#ffff00' if percentage >= 50 else '#ff6600'
        return format_html(
            '<div style="width: 100px; background-color: #ddd;">'
            '<div style="width: {}%; background-color: {}; height: 20px;"></div>'
            '</div>',
            percentage, color
        )
    proficiency_bar.short_description = 'Level'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'tagline', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'website_url')
        }),
        ('Resume', {
            'fields': ('resume_file',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not About.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of the singleton instance
        return False


# Customize admin site headers
admin.site.site_header = 'Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Welcome to Your Portfolio Admin Panel'
