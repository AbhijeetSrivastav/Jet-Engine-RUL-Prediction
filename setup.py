"Install all required libraries"

from setuptools import find_packages, setup
from typing import List


REQUIREMENTS_FILE = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements()->List[str]:
    "Fetch required libraries from requirements file"
    with open(REQUIREMENTS_FILE) as requirements_file:
        requirement_list = requirements_file.readlines()
        requirement_list = [requirement.replace("\n",  "") for requirement in requirement_list]
        

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    
    return requirement_list


setup(
    name = "Jet-Engine-RUL-Prediction",
    version = "0.0.1",
    author = "Abhijeet Srivastav",
    author_email = "abhijeetsrivastav292@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)