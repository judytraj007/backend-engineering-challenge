from setuptools import setup, find_packages

setup(
	name='unbabel_cli',
	version='0.0.0',
	packages=find_packages(),
	install_requires=[
		'click'
	],
	entry_points={"console_scripts": ["unbabel_cli=unbabel_cli:main"]},
	description='A cli app to calculate the moving average of translation delivery times'
)