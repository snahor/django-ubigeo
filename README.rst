django-ubigeo
=============

Overview
--------

Ubigeo is a coding system for geographical locations used in Peru. There
are two types of codes: the one used by RENIEC and the other one by INEI.
This django app provides RENIEC codes, because it’s the one used in the
national IDs.

Requires:

-  ``python 3.4``
-  ``django 1.7``

Installation
------------

From PYPI:

::

    pip install django-ubigeo

From GitHub

::

    pip install git+git://github.com/snahor/django-ubigeo

Then add ``ubigeo`` to your ``INSTALLED_APPS``.

::

    INSTALLED_APPS = (
        ...
        'ubigeo',
        ...
    )

To apply the migration file provided:

::

    ./manage.py migrate ubigeo

Models
------

The main model is ``Ubigeo``. It has a self reference ``parent``.

Fields
~~~~~~

-  ``name``
-  ``parent``
-  ``reniec`` RENIEC code.
-  ``inei`` INEI code.

There are three more models, which are proxy.

-  ``Department``
-  ``Province``
-  ``District``

Examples
^^^^^^^^

::

    >>> district = District.objects.filter(name='SANTIAGO DE SURCO')
    >>> province = district.parent
    >>> print(province.pk, province.reniec, province.name)
    1386 1401 LIMA
    >>> department = province.parent
    >>> print(department)
    LIMA
    >>> print(department.pk)
    1385
    >>> provinces = list(Province.objects.filter(parent=department))
    >>> print(len(provinces))
    10

What else is included?
----------------------

Forms
~~~~~

-  ``DepartmentForm``: A simple dropdown with all the departments.
-  ``ProvinceForm``: Two dropdowns: department and province.
-  ``UbigeoForm`` (alias for ``DistrictForm``): Three dropdowns: department, province and district.

Example
^^^^^^^

::

    from django import forms
    from ubigeo.forms import UbigeoForm
    from .models import MyModel


    class MyForm(UbigeoForm, forms.ModelForm):
        class Meta:
            model = MyModel

Endpoints
~~~~~~~~~

-  ``departments/``: List all the departments.
-  ``departments/(\d+)/provinces/`` List all the provinces belonging to a department. A department id is needed.
-  ``provinces/(\d+)/districts/`` List all the districts belonging to a province. A province id is needed.

Each of these endpoints returns data in JSON format with this structure:

::

    {
      "data": [
        ...
        {
          "id": 0,
          "name": "",
          "parent_id": null
        }
        ...
      ]
    }
