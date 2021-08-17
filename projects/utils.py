
from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginate_projects(request, projects_obj, results):
    page = request.GET.get('page')
    paginator = Paginator(projects_obj, results)

    try:
        projects_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects_obj = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects_obj

def search_projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects_obj = Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags))

    return projects_obj, search_query
