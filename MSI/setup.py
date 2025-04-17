from setuptools import setup, find_packages

setup(
    name='MSI',
    version='1.0',
    description='Un package python pour les opérations mathématiques courantes',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown", 
    url="https://MSI.readthedocs.io",
   

    project_urls={
        'Documentation': 'https://INFO3.com/readthedocs.io',  # Ajoutez ici la documentation si applicable
        'Source': 'https://github.com/nabilsoft237/DOCS',
    },
    author='ngouhouo nabil',
    author_email='nabilf045@gmail.com',
    packages=find_packages(),
    classifiers=[
            "Programming Language :: python :: 3",
            "Operating System :: OS Independent ",
            "Licence :: OSI Aproved :: MIT"

    ],
    install_requires=[],

)