from django.shortcuts import render, get_object_or_404
from core.models import Project


def home(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'home.html', context)


def endpoints(request, project):
    context = {'endpoints': get_object_or_404(Project, slug=project).endpoints.all()}
    return render(request, 'project.html', context)
