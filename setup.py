import os
from setuptools import find_packages, setup
from eponym import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
	README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='eponym',
	version=__version__,
	packages=find_packages(),
	include_package_data=True,
	license='MIT License',
	description='Decent username generator based on handpicked wordlists',
	long_description=README,
	long_description_content_type='text/markdown',
	url='https://github.com/DoctorJohn/eponym',
	author='Jonathan Ehwald',
	author_email='pypi@ehwald.info',
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
)
