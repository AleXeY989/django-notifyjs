
from setuptools import setup

setup(
    name='django-bxslider',
    version='1.5.10',
    url='https://github.com/AleXeY989/django-bxslider.git',
    description='Django package for jquery-bxslider: A lightweight customizable lightbox plugin for jQuery',
    author='Jack Moore',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'bxslider'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django-bxslider'],
    package_data={'django_bxslider': ['static/js/*.js']}
)
