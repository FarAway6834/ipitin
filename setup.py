from setuptools import setup, find_packages

setup(
    name='ipitin',
    version='0.0.1',
    description='Import Pandas Import Tenserflow Import Numpy',
    author='faraway6834',
    author_email='faway6834@gmail.com',
    url='https://github.com/FarAway6834/ipitin',
    install_requires=['pandas', 'tenserflow', 'numpy'],
    packages=find_packages(exclude=[]),
    keywords=['import pandas', 'import fenserflow', 'import numpy', 'Import Pandas Import Tenserflow Import Numpy', 'ipitin', 'FarAway6834'],
    python_requires='>=3.8',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ]
)
