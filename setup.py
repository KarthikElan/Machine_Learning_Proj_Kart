from gettext import install
from xml.etree.ElementTree import VERSION
from setuptools import setup,find_packages
from typing import List 

#Declaring Variables for set up func
PROJECT_NAME="Housing Predictor"
VERSION="0.0.11"
AUTHOR="Karthik Elangovan"
DESCRIPTION="First FSDS ML Project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function returns list of requirements in 
    requirements.txt file

    return: return list of which contain name of libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)

 

