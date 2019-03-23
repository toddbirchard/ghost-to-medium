from setuptools import setup, find_packages, tests_require, packages, name

with open("README", 'r') as f:
    long_description = f.read()

setup = (
    name='ghost-to-medium',
    version='1.0',
    description='Endpoint which creates a post in a Medium publication.',
    long_description=long_description,
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    url="https://github.com/toddbirchard/ghost-to-medium",
    packages=['medium'],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
    install_requires=[
        "requests",
        "flask",
        "flask_redis"
    ]
)
