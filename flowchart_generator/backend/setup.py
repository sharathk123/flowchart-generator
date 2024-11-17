from setuptools import find_packages, setup
from typing import List
from pathlib import Path

def get_requirements() -> List[str]:
    """
    This function will return a list of requirements
    from the requirements.txt file.
    """
    requirement_list: List[str] = []
    
    # Get the absolute path to the requirements.txt file
    requirements_file_path = Path(__file__).parent / "requirements.txt"

    # Open and read the requirements.txt file
    try:
        with open(requirements_file_path, 'r') as f:
            # Read the file and strip any leading/trailing whitespace
            requirement_list = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: {requirements_file_path} file not found!")

    return requirement_list

setup(
    name="flowchart_generator",  # Project name
    version="0.0.1",
    author="Sharath",
    author_email="sharath.babuk@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  # Automatically read dependencies
)
