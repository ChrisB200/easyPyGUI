from setuptools import setup, find_packages

setup(
    name="easyPyGUI",
    version = "0.1.0",
    author="Christopher Bonner",
    author_email="cbonner.dev@outlook.com",
    description="This is a python library for pygame that makes it easier to create user interfaces quickly",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)