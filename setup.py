from os import path

from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='weasel-cli',
    version='1.0.0',
    description='Simulate Dawkins\' weasel experiment',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['weasel'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        weasel=weasel:cli
    ''',
    url='https://github.com/wdsrocha/weasel-cli',
    license='MIT',
)