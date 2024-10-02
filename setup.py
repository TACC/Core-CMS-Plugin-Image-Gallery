import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# To allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms-tacc-image-gallery',
    version='0.1.4',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A DjangoCMS plugin (for TACC Core CMS) to create an image gallery.',
    long_description=README,
    url='https://github.com/TACC/Core-CMS-Plugin-Image-Gallery/',
    author='TACC ACI WMA, TACC COA CMD',
    author_email='wma-portals@tacc.utexas.edu, coa-cmd@tacc.utexas.edu',
    # SEE: https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=[
        'Django>=2.2.27',
        'django-cms>=3.7.4,<4',
        'django-sekizai>=2.0',
        'djangocms-picture>=3.0,<4.0',
    ],
    # SEE: https://pypi.org/classifiers/
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.16',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
