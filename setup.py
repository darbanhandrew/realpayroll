from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in realpayroll/__init__.py
from realpayroll import __version__ as version

setup(
	name="realpayroll",
	version=version,
	description="Real Agro payroll system customized",
	author="Mohammad Darban Baran",
	author_email="darbanhandrew@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
