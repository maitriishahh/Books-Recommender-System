from setuptools import setup, find_packages

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()


REPO_NAME = 'Books Recommender System'
AUTHOR_USER_NAME = 'Maitri Shah'
SRC_REPO = 'books_recommender'
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version='0.0.1',
    author='Maitri Shah',
    description='A small local packages for End to End books recommendations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/maitriishahh/Books-Recommender-System",
    author_email='maitrishah142004@gmail.com',
    packages=find_packages(),
    license='MIT',
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS)