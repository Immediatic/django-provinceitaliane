from setuptools import setup, find_packages

setup(
    name = 'django-provinceitaliane',
    version = '0.1.2',
    description = 'Province e Regioni Italiane for Django',
    author = 'Francesco Facconi',
    url = 'http://code.google.com/p/django-provinceitaliane/',
    packages = find_packages(),
    zip_safe=False,
    package_data = {
        '': ['fixtures/initial_data.json', 'locale/*/*/*'],
    },
)