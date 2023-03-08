from setuptools import setup, find_namespace_packages

setup(
    name='adv-subgit',
    version='0.0.1',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'cadet-cli',
    ],
    entry_points = {
        #  we are a supplying an entry point under the group cadet.cli
        'cadet.cli': [
            'subcommand = cadet.subgit.cli:test'
            
        ]
    }
)
