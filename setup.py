from setuptools import setup


setup(
    name='django-ubigeo',
    version='0.0.1',
    description='Ubigeo models, forms and views for Django',
    author='Hans Roman',
    author_email='hans@roman.pe',
    url='http://github.com/snahor/django-ubigeo',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    keywords=['ubigeo', 'django'],
    zip_safe=False,
    packages=['ubigeo', 'ubigeo.migrations'],
    package_data={
        'ubigeo': ['data/*.json'],
    }
)
