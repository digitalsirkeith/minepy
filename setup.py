from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='minepy',
   version='1.0',
   description='Inspired by Mineflayer and pyCraft. A high-level API for creating minecraft client bots using Python.',
   license="MIT",
   long_description=long_description,
   author='Keith Vargas',
   author_email='keith.vargas@ieee.org',
   packages=['minepy']
)