from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects_obj = Project.objects.all()
    context = {'projects': projects_obj}
    return render(request, 'projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'single-projects.html', {'project': project_obj})


def create_project(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "project_form.html", context)
