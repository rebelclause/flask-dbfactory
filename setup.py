"""
Flask-DBFactory
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-DBFactory',
    version='1.0',
    url='http://example.com/flask-sqlite3/',
    license='BSD',
    author='Tim Pozza',
    author_email='dbfactory@sunlasso.com',
    description='Simple import method, to inline SQLAlchemy DB/model creation, for fast ORM prototyping setups.',
    long_description=__doc__,
    # py_modules=['flask_dbfactory'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_dbfactory'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'Flask-SQLAlchemy'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
