from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns the list of requirements from requirements.txt
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.strip() for req in requirements if req.strip() != '-e .']
    return requirements



setup(
name = 'mlproject',
version = '0.0.1',
author = 'Harisankar',
author_email = 'harisankard19@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)