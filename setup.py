from setuptools import setup

setup(
    name='dawkins-weasel-simulation',
    version='0.1',
    py_modules=['weasel'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        weasel=weasel:cli
    ''',
)