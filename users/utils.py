from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatorProfiles(request, profiles,result):
    page = request.GET.get('page')
    pagination = Paginator(profiles, result)
    try:
        profiles = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        profiles = pagination.page(page)
    left_range = (int(page)-4)
    if left_range < 1:
        left_range = 1
    right_range = (int(page)+5) + 1
    if right_range > pagination.num_pages + 1:
        right_range = pagination.num_pages + 1
    custome_range = range(left_range, right_range)
    return profiles, pagination, custome_range


def searchProfile(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    return profiles, search_query