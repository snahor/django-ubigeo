from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(
        r'^departments/',
        'ubigeo.views.departments',
        name='departments'
    ),
    url(
        r'^provinces/(\d+)',
        'ubigeo.views.provinces',
        name='provinces'
    ),
    url(
        r'^districts/(\d+)',
        'ubigeo.views.districts',
        name='districts'
    ),
)
