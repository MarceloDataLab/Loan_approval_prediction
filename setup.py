# setup.py
from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='Loan_approval_prediction',
      description="Python package designed to predict if your loan will be approved or rejected. Utilizing machine learning algorithms",
      packages=find_packages(),
      install_requires=requirements)
