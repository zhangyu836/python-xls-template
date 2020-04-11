import os
from setuptools import setup

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(CUR_DIR, "README.md")
with open("README.md", "r") as fd:
    long_description = fd.read()

setup(
    name = 'xlstpl',
    version = "0.2",
    author = 'Zhang Yu',
    author_email = 'zhangyu836@gmail.com',
    url = 'https://github.com/zhangyu836/python-xls-template',
    packages = ['xlstpl'],
	install_requires = ['xlrd', 'xlwt', 'openpyxl', 'jinja2', 'six'],
    description = ( 'A python module to generate xls files from a xls template' ),
    long_description = long_description,
    long_description_content_type = "text/markdown",
    platforms = ["Any platform "],
    license = 'MIT',
    keywords = ['xls', 'spreadsheet', 'workbook', 'template']
)