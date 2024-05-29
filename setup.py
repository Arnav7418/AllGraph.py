# setup.py
from setuptools import setup, find_packages

setup(
    name='allgraph',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library for creating various types of graphs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/allgraph',  # Update with your actual repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
