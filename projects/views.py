from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': "E-commerce Website 1",
        'description': 'Fully functional E-commerce Website 1'
    },
    {
        'id': '2',
        'title': "E-commerce Website 2",
        'description': 'Fully functional E-commerce Website 2'
    },
    {
        'id': '3',
        'title': "E-commerce Website 3",
        'description': 'Fully functional E-commerce Website 3'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'single-projects.html', {'project': project_obj})
