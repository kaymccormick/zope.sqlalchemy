from setuptools import setup, find_packages
import sys, os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

setup(name='zope.sqlalchemy',
      version=version,
      description="Minimal Zope/SQLAlchemy transaction integration",
      long_description=read('src', 'zope', 'sqlalchemy', 'README.txt'),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Zope3",
        "Programming Language :: Python",
        "License :: OSI Approved :: Zope Public License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Laurence Rowe',
      author_email='laurence@lrowe.co.uk',
      url='http://svn.zope.org/zope.sqlalchemy',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zope'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',
          'SQLAlchemy>=0.4.6.dev-r4655,==dev',
          'transaction',
          'zope.interface',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      extras_require = dict(
              test = ['zope.testing'],
              ),
      )
