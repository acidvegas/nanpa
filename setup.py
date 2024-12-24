#!/usr/bin/env python
# North American Numbering Plan Administration (NANPA) API Client - Developed by acidvegas in Python (https://git.acid.vegas/nanpa)
# setup.py

from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as fh:
	long_description = fh.read()

setup(
	name='nanpa',
	version='1.0.0',
	author='acidvegas',
	author_email='acid.vegas@acid.vegas',
	description='North American Numbering Plan Administration (NANPA) API Client',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/acidvegas/nanpa',
	project_urls={
		'Source Code': 'https://github.com/acidvegas/nanpa',
	},
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Communications :: Telephony',
	],
	packages=find_packages(),
	python_requires='>=3.6',
)
