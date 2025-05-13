from setuptools import setup, find_packages
setup(
   name="H.U.B",
   description='Stands for the "Helpful Ubiquitous Buddy"',
   version="0.1",
   packages=find_packages(),
   entry_points={
        'console_scripts': ['hub=hub.__main__:main'], 
    },
)