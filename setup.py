from setuptools import setup, find_packages


setup(
    name='django-ubigeo',
    version='0.0.1',
    description='',
    author='Hans Roman',
    author_email='hans@roman.pe',
    url='http://github.com/snahor/django-ubigeo',
    packages=find_packages(include=('ubigeo',)),
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=['django>=1.7'],
    keywords=['ubigeo', 'django'],
    extras_require={
        'test': ['pytest', 'pytest-django']
    }
)
