from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(
        r'^departments/$',
        'ubigeo.views.departments',
        name='departments'
    ),
    url(
        r'^departments/(\d+)/provinces/$',
        'ubigeo.views.provinces',
        name='provinces'
    ),
    url(
        r'^provinces/(\d+)/districts/$',
        'ubigeo.views.districts',
        name='districts'
    ),
)
