from setuptools import setup, find_packages

install_requires = [
    'behave >= 1.2.6',
    'requests >= 2.11.1',
    'nose >= 1.3.7',
    'flask >= 1.1.1'
]

setup(
   name='Flask Tests',
   version='0.0.1',
   maintainer='Music Group Research UK (Test Packages)',
   maintainer_email='linux-packages@music-group.com>',
   description='Mcloud Tests Module',
   packages=find_packages(),
   platforms=['any'],
   install_requires=install_requires,
)