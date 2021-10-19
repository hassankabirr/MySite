from django.db.models import Q
from .models import Project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatorProjects(request, projects,result):
    page = request.GET.get('page')
    pagination = Paginator(projects, result)
    try:
        projects = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        projects = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        projects = pagination.page(page)

    left_range = (int(page) - 4)
    if left_range < 1:
        left_range = 1
    right_range = (int(page) + 5) + 1
    if right_range > pagination.num_pages + 1:
        right_range = pagination.num_pages + 1
    custome_range = range(left_range, right_range)

    return projects, pagination, custome_range

def searchProjects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query
