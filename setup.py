from setuptools import setup, find_packages

install_requires = [
    'behave >= 1.2.6',
    'flask >= 1.1.1',
    'flask_api >= 1.1'
]

setup(
   name='endpoints',
   version='0.0.1',
   maintainer='Music Group Research UK (Test Packages)',
   maintainer_email='linux-packages@music-group.com>',
   description='endpoints for the flask project',
   packages=find_packages(),
   platforms=['any'],
   install_requires=install_requires,
)
