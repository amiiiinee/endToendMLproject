# from setuptools import setup, find_packages


# HYPEN_E_DOT = '-e .'
# def get_requirements(file_path):
#     with open(file_path, 'r') as file:
#         requirements = file.readlines()
#         requirements = [req.strip() for req in requirements]
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements
# setup(
#     name='ml_project',
#     version='0.1.0',                         
#     author='amine',
#     author_email='mohamedamineg@example.com',
#     package=find_packages(),
#     install_requires=get_requirements('requirements.txt'),
# )

from setuptools import setup, find_packages

def get_requirements(file_path):
    """Read requirements.txt and return a list of dependencies"""
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
    return requirements

setup(
    name='ml_project',
    version='0.1.0',
    author='amine',
    author_email='mohamedamineg@example.com',
    packages=find_packages(),  # FIXED: packages instead of package
    install_requires=get_requirements('requirements.txt'),
)
