from unicodedata import category
from django.shortcuts import render
from .models import Project, Result, SmmProject
from django.http import JsonResponse
from django.conf import settings
from .forms import ReceiveContactForm
from .models import ContactUs


from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /moderator/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def index(request):
    projects = Project.objects.all()

    result_is = Result.objects.filter(pk=1).exists()

    result = None

    if result_is:
        result = Result.objects.get(pk=1)

    context = {
        'projects': projects,
        'result': result
    }
    return render(request, 'core/index.html', context)


def about(request):
    result = Result.objects.get(pk=1)

    result_is = Result.objects.filter(pk=1).exists()
    
    result = None

    if result_is:
        result = Result.objects.get(pk=1)

    context = {
        'result': result,
    }
    return render(request, 'core/about.html', context)


def contact(request):
    contact_info = ContactUs.objects.get(pk=1)

    if request.method == 'POST':
        form = ReceiveContactForm(request.POST)

        if form.is_valid():
            form.save()

            form = ReceiveContactForm()

    context = {
        'contact_info': contact_info
    }
            
    return render(request, 'core/contact.html', context)


def projects_api(request):
    qs = request.GET.get('filter')

    projects = Project.objects.all()

    if qs == 'all':
        projects = Project.objects.all()
    elif qs == 'smm':
        projects = Project.objects.filter(category__id=1)
    elif qs == 'branding':
        projects = Project.objects.filter(category__id=2)

    elif qs == 'logo':
        projects = Project.objects.filter(category__id=4)

    elif qs == 'extra':
        projects = Project.objects.filter(category__id=5)
    
    response = []
    url = request.build_absolute_uri('/')[:-1]

    for project in projects:
        response.append({
            'id': project.id,
            'title': project.title,
            'image': project.image.url,
            'url':  f'{url}/project/{project.slug}/'
        })

    return JsonResponse({'response': response}, safe=False)


def portfolio(request):
    
    return render(request, 'core/portfolio.html')


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        'project': project
    }
    
    return render(request, 'core/project_detail.html', context)


def error_404(request, exception):
    return render(request, "core/404.html")
