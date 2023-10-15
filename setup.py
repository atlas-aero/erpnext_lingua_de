from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lingua_de/__init__.py
from lingua_de import __version__ as version

setup(
	name="lingua_de",
	version=version,
	description="Better German translations and adaptations",
	author="AtlasAero GmbH",
	author_email="info@atlasaero.eu",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
