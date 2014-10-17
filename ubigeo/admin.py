from django.contrib import admin
from .models import Department, Province, District


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ('name', 'parent')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    fields = ('name', 'parent')
