import os
from setuptools import setup,find_packages

DESCRIPTION = "Library with major data structures and algorithms"

here=os.path.abspath(os.path.dirname(__file__))

try:
	with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
		long_description=f.read()
except FileNotFoundError:
	long_description = DESCRIPTION

setup(
	name="dsalgo",
	version="0.0.0.1a",
	author="Kapil",
	author_email="kapilbansal.gbpecdelhi@gmail.com",
	description="data structures and algorithms library",
	long_description=long_description,
	download_url="https://github.com/codesankalp/dsalgo",
	platforms = ['Platform Independent'],
	keywords = ['python', 'algorithms', 'data structures'],
	packages = find_packages(),
	install_requires = [],
	classifiers = [
		'Development Status :: 1-Alpha',
		'Intended Audience :: Programmers'
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.9',
	],
	)
