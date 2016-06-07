from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='immunarray.lims',
      version=version,
      description="",
      long_description=open("README.md").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Immunarray',
      author_email='justin.pitts@immunarray.com',
      url='http://www.immunarray.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['immunarray'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.principalsource',
          'collective.z3cform.datagridfield',
          'magnitude',
      ],
      extras_require={
          'test': [
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
