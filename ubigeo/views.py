from django.http import JsonResponse
from .models import Department, Province, District


def _generic_response(queryset):
    return JsonResponse({
        'data': [
            {'name': item.name, 'id': item.pk}
            for item in queryset
        ]
    })


def departments(request):
    return _generic_response(
        Department.objects.all()
    )


def provinces(request, department):
    return _generic_response(
        Province.objects.filter(parent=department)
    )


def districts(request, province):
    return _generic_response(
        District.objects.filter(parent=province)
    )
