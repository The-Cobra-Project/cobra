from setuptools import setup, find_packages

setup(
    name='cobra-engine',
    version='1.0.0',
    author='Ron Shani',
    author_email='ronshan4u@gmail.com',
    description='A tiny portable OpenGL framework using PyGame',
    packages=find_packages(),
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)