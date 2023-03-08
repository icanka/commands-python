from setuptools import setup, find_namespace_packages

setup(
    name='cadet-cli',
    version='0.0.1',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'cadet = cadet.cli.entry:cadet',
        ]
    }

)
