from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from core.models import Project

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'contact', 'portfolio', 'brand', 'smm', 'extra']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()
    
    def lastmode(self,obj):
        return obj.created_at