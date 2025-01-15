from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    WE ARE PROVIDING ALL THE REQUIRED LIBRARIES

    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        HYPEN_E_DOT = '-e .'

        if HYPEN_E_DOT in requirements:
            requirements.remove( HYPEN_E_DOT)
            
    return requirements


setup(
    name='ML Project',
    version='0.0.1',
    author='MUPPALLA KOMAL',
    author_email='muppallakomaliitkgp2022@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )