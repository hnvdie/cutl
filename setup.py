from setuptools import setup, find_packages

setup(
    name="cutl",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cutl=cutl.cli:main',
        ],
    },
)
