import setuptools
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name="CryptoBaker",
    version="0.0.1",
    description="Crypto Bakery",
    long_description=read("README.md"),
    url="https://github.com/AgeOfMarcus/CryptoBaker",
    author="AgeOfMarcus",
    author_email="marcus@marcusweinberger.com",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=[],
)