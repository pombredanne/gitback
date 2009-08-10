from setuptools import setup, find_packages

version = '0.0'

setup(name='gitback',
      version=version,
      description="Backing up git repositories and using git for backups",
      long_description=open('README.txt').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='http://pypi.python.org/pypi/gitback',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      scripts=['scripts/git-back',
               'scripts/git-get-blobs',
               'scripts/git-rm-blobs'],
      )
