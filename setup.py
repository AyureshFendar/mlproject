from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    Removes any occurrences of '-e .' which is used for editable installs.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Ayuresh Fendar",
    author_email="ayureshfendar2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
