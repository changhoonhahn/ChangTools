from setuptools import setup, find_packages
import os, sys

__version__ = '0.1'

setup(name = 'ChangTools',
      version = __version__,
      description = 'Tools that Chang uses',
      author='ChangHoon Hahn',
      author_email='chh327@nyu.edu',
      url='',
      platforms=['*nix'],
      license='GPL',
      requires = ['numpy','pyfits','numpy','matplotlib','scipy'],
      provides = ['ChangTools'],
      packages = ['ChangTools'],
      scripts=['ChangTools/plotting.py', 'ChangTools/fitstables.py']
)
