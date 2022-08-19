from django.shortcuts import render
from core.models import Project, SmmProject

def brand_service(request):
    projects = Project.objects.filter(category=(2,3))

    context = {
        'projects': projects
    }
    return render(request, 'service/brand.html', context)


def smm_service(request):
    projects = Project.objects.filter(category=1)
    smm_projects = SmmProject.objects.all()

    context = {
        'projects': projects,
        'smm_projects': smm_projects
    }
    return render(request, 'service/smm.html', context)


def extra_service(request):
    projects = Project.objects.filter(category=4)

    context = {
        'projects': projects,
    }
    return render(request, 'service/extra.html', context)


def web_service(request):
    projects = Project.objects.filter(category=4)

    context = {
        'projects': projects,
    }
    return render(request, 'service/web.html', context)
