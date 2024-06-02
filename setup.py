from setuptools import setup, find_packages
setup(
name='app',
version='1.0',
packages=find_packages(),
install_requires=[
'flask',
'pathlib',
'pandas',
'numpy',
'scikit-learn',
'requests',
'pickle',
'zipfile',
'time',
'os'
],
)