import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.5.2',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'SQLAlchemy==0.9.8',
    'waitress',
    'zope.sqlalchemy==0.7.5',
]

setup(name='pony',
      version='0.0',
      description='pony',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pony",
      entry_points="""
      [paste.app_factory]
      main = pony:main
      [console_scripts]
      initialize_pony_db = pony.scripts.initializedb:main
      """,
      )
