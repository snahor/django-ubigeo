from django.db import models
from django.db.models import Q

__all__ = ('Ubigeo', 'Department', 'Province', 'District',)


class Ubigeo(models.Model):
    name = models.CharField(
        max_length=200
    )
    reniec = models.CharField(
        max_length=6,
        blank=True
    )
    inei = models.CharField(
        max_length=6,
        blank=True
    )
    parent = models.ForeignKey(
        'Ubigeo',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<%s (%s)>' % (self.__class__.__name__, self.reniec)


class DepartmentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)


class Department(Ubigeo):
    objects = DepartmentManager()

    class Meta:
        proxy = True
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class ProvinceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            ~Q(parent=None),
            reniec__regex=r'^\d{4}$'
        )


class Province(Ubigeo):
    objects = ProvinceManager()

    class Meta:
        proxy = True


class DistrictManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            ~Q(parent=None),
            reniec__regex=r'^\d{6}$'
        )


class District(Ubigeo):
    objects = DistrictManager()

    class Meta:
        proxy = True
