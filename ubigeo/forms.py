from django import forms
from .models import Department, Province, District


class DepartmentForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects
    )


class ProvinceForm(DepartmentForm):
    province = forms.ModelChoiceField(
        queryset=Province.objects.none()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound:
            department = self._get_field_value('department')
            if department:
                self.fields['province'].queryset = Province.objects.filter(
                    parent=department
                )

    def _get_field_value(self, name):
        field = self.fields[name]
        value = field.widget.value_from_datadict(
            self.data,
            self.files,
            self.add_prefix(name)
        )
        try:
            return field.clean(value)
        except:
            return None


class DistrictForm(ProvinceForm):
    district = forms.ModelChoiceField(
        queryset=District.objects.none()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound:
            province = self._get_field_value('province')
            if province:
                self.fields['district'].queryset = District.objects.filter(
                    parent=province
                )


UbigeoForm = DistrictForm
