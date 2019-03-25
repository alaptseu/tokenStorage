from setuptools import setup, find_packages, __version__
from codecs import open
import os

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()

exec(read('core/version.py'))

setup(
    name='Token Storage CLI',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    # development metadata
    zip_safe=True,

    install_requires=[
        'click',
        'requests',
        'tinydb',
        'terminaltables',
    ],
    entry_points='''
        [console_scripts]
        core=core.cli:cli
    ''',
)