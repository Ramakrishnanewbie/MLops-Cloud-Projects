from typing import List
from setuptools import setup,find_packages

def get_requirements(file_path : str) -> List[str]:
    requirements=[]
    with open(file_path) as f:
        x=f.readlines()
        requirements=[req.replace("\n","") for req in x]
        if '-e .' in requirements:
            requirements.remove('-e .')
        return requirements
    

setup(
    name='rk',
    version='0.0.1',
    author='Rama',
    author_email='abcd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)