import os
import re
import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def get_metadata(package, field):
    """
    Return package data as listed in `__{field}__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__init__.py'), encoding='utf-8').read()
    return re.search("^__{}__ = ['\"]([^'\"]+)['\"]".format(field), init_py, re.MULTILINE).group(1)


setup(
    name='puput',
    version=get_metadata('puput', 'version'),
    packages=find_packages(exclude=("example*", "tests*")),
    include_package_data=True,
    keywords="django wagtail puput blog cms app",
    description='A Django blog app implemented in Wagtail.',
    long_description=codecs.open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8').read(),
    install_requires=[
        'Django>=3.0,<4.2',
        'wagtail>=3.0,<4.2',
        'django-el-pagination@git+https://github.com/APSL/django-el-pagination.git@4.0.0',
        'django-social-share>=1.3.0',
        'django-colorful>=1.3'
    ],
    url='http://github.com/APSL/puput',
    author=get_metadata('puput', 'author'),
    author_email=get_metadata('puput', 'email'),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)