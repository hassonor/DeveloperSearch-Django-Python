from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm
from .utils import search_projects, paginate_projects


def projects(request):
    projects_obj, search_query = search_projects(request)
    custom_range, projects_obj = paginate_projects(request, projects_obj, 6)

    context = {'projects': projects_obj, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)



def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-projects.html', {'project': project_obj})


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project was deleted successfully!')
        return redirect('projects')

    context = {'object': project}
    return render(request, "delete_template.html", context)
