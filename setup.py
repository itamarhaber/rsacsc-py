from setuptools import setup, find_packages

setup(
    name='rsacsc-py',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/itamarhaber/rsacsc-py',
    install_requires=[
        'redis',
    ],
    author="Itamar Haber"
)
