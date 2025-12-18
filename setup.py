from setuptools import setup, find_packages


HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='ml_project',
    version='0.1.0',                         
    author='amine',
    author_email='mohamedamineg@example.com',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)