
from setuptools import setup

setup(
    name='django-bxslider',
    version='4.1.2',
    url='https://github.com/AleXeY989/django_bxslider.git',
    description='Django package for jquery-bxslider: The Responsive jQuery Content Slider',
    author='Steven Wanderski',
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
    packages=['django_bxslider'],
    package_data={'django_bxslider': ['static/js/django_bxslider/*.js', 'static/css/django_bxslider/*.css', 'static/img/django_bxslider/*.gif', 'static/img/django_bxslider/*.png']}
)
