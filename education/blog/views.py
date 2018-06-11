from django.shortcuts import render

from blog.models import School


def school_list(request, school_id):
    school_list = School.objects.get(id=school_id)
    context = {
        'school_list': school_list
    }
    return render(request, 'school', context)