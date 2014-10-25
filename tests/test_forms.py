from ubigeo.forms import UbigeoForm
from ubigeo.models import District


def test_ubigeo_form(db):
    district = District.objects.filter(name='SANTIAGO DE SURCO').first()
    data = {'department': '', 'province': '', 'district': district.pk}
    form = UbigeoForm(data)
    assert not form.is_valid()

    province = district.parent
    data['province'] = province.pk
    form = UbigeoForm(data)
    assert not form.is_valid()

    department = province.parent
    data['department'] = department.pk
    form = UbigeoForm(data)
    assert form.is_valid()

    # arequipa
    miraflores = District.objects.filter(name='MIRAFLORES').first()
    data['district'] = miraflores.pk
    form = UbigeoForm(data)
    assert not form.is_valid()
