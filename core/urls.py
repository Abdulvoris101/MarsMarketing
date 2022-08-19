from django.urls import path
from .views import index, about, contact, project_detail, projects_api, portfolio

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    
    path('portfolio/', portfolio, name='portfolio'),
    path('project/<slug:slug>/', project_detail, name='project_detail'),

    # Api

    path('api/projects/', projects_api, name='projects'),
]


