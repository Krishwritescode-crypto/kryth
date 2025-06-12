from setuptools import setup, find_packages

setup(
    name='kryth',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kryth = kryth.cli:run_kryth'
        ],
    },
    install_requires=[
        'sympy'
    ],
    author='Krish Majumdar',
    description='KRYTH: A compact math-first language for problem solvers',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/kryth',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
)
