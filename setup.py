'''
The setup.py file is essential part of packaging and distributing Python projects.it is used
by setuptools, a popular library for packaging Python projects. 
The setup.py file contains metadata about the project and instructions on how to install it.'''

from setuptools import setup, find_packages
# find_packages() automatically discovers all packages and subpackages in the project directory 
# by looking for __init__.py files in every directory.
from typing import List

def get_requirements() -> List[str]:
    """"
    This function will return the list of requirements
    """
    requirement_lst: List[str] = []
    try:
            ## Open the requirements.txt file in read mode
        with open('requirements.txt','r') as file:
            ## Read lines from the file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                if requirement and  requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError: 
            print("The requirements.txt file was not found.")     

    return requirement_lst    

setup(
    name='NetworkSecurity', 
    version='0.0.1',
    author='Rahul',
     author_email="rahulkrmishra2004@gmail.com"  ,
    packages=find_packages(),
    install_requires=get_requirements(),
)     
            