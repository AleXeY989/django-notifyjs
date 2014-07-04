
from setuptools import setup

setup(
    name='django-notifyjs',
    version='v0.3.1',
    url='https://github.com/AleXeY989/django-notifyjs.git',
    description='Django package for jquery-notifyjs: Notify.js is a jQuery plugin to provide simple yet fully customisable notifications.',
    author='Jaime Pillora',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'notifyjs'],
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
    packages=['django_notifyjs'],
    package_data={'django_notifyjs': ['static/django_notifyjs/js/*.js']}
)
