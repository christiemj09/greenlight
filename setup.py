"""
Install greenlight.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Make processes wait for events.',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/greenlight.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': [],
		'packages': ['greenlight'],
		'scripts': [],
		'entry_points': {
		    'console_scripts': [],
		},
		'name': 'greenlight',
	}

	setup(**config)	

if __name__ == '__main__':
	main()
