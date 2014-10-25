import pytest
from ubigeo.models import District


@pytest.mark.django_db
def test_endpoints(client, settings):
    settings.ROOT_URLCONF = 'ubigeo.urls'

    surco = District.objects.filter(name='SANTIAGO DE SURCO').first()
    lima_province = surco.parent
    lima_department = lima_province.parent

    response = client.get('/departments/')
    assert response.status_code == 200

    response = client.get('/departments/%s/provinces/' % lima_department.pk)
    assert response.status_code == 200

    response = client.get('/provinces/%s/districts/' % lima_province.pk)
    assert response.status_code == 200
