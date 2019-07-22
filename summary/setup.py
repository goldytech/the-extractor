from setuptools import setup, find_packages

setup(
    name='nlpsummary',
    version='0.0.1',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    url='goldytech.wordpress.com',
    license='MIT',
    author='Muhammad Afzal Qureshi',
    author_email='afzal.qureshi@outlook.com',
    description='Generic implementation of text summary',
    install_requires=['spacy'],
    python_requires='>=3.7'
)
