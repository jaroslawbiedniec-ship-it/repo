"""Setup script for Book Manager."""
from setuptools import setup, find_packages

setup(
    name="book_manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "sqlite3",
    ],
    entry_points={
        "console_scripts": [
            "book-manager=main:main",
        ],
    },
)