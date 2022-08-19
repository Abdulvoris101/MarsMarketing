from django.contrib import admin
from .models import Company, ContactUs, Project, ProjectImage, Category, Result, SmmProject, ReceiveContact
from django.contrib.admin.decorators import register
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin


@register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('id', 'image_tag')
    list_display_links = ('id', 'image_tag' )
    ordering = ('id', )

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id', )

@register(Project)
class ProjectAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag', 'created_at')
    search_fields = ('title', )
    ordering = ('-created_at', )
    prepopulated_fields = {"slug": ("title",)}

    inlines = [ProjectImageInline]

@register(ContactUs)
class ContactAdmin(TranslationAdmin):
    fields = ('address', 'email_address', 'phone_number', 'working_hours')
    

admin.site.register(ProjectImage)
admin.site.register(Result)
admin.site.register(SmmProject)
admin.site.register(ReceiveContact)
