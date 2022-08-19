from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from core.views import robots_txt

from .sitemaps import StaticViewSitemap, ProjectSitemap

sitemaps = {'static': StaticViewSitemap, 'project': ProjectSitemap}

urlpatterns = [
    path('moderator/', admin.site.urls),
    path('robots.txt/', robots_txt),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] 



urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('service/', include('service.urls')),
)




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.error_404'