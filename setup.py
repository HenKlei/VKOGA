from setuptools import setup, find_packages


dependencies = [
    'numpy',
    'scipy',
    'matplotlib',
    'scikit-learn'
]

setup(
    name='vkoga',
    version='0.1.0',
    description='Python implementation of the Vectorial Kernel Orthogonal Greedy Algorithm',
    author='Gabriele Santin, Tizian Wenzel',
    maintainer='Tizian Wenzel',
    packages=find_packages(),
    install_requires=dependencies,
)
