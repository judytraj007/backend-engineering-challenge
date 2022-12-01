from setuptools import setup, find_packages

setup(
	name='unbabel_cli',
	version='0.0.0',
	packages=find_packages(),
	install_requires=[
		'click'
	],
	entry_points='''
	[console_scripts]
	unbabel_cli=unbabel_cli:parse_input
	'''
)