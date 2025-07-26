from setuptools import setup, find_packages

setup(
    name='ec_scalar_mult',
    version='0.1.0',
    description='Elliptic Curve Scalar Multiplication in Python using ecdsa',
    author='Cyprian Sakwado',
    packages=find_packages(),  # Automatically finds your packages
    install_requires=[
        'ecdsa>=0.19.0'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
