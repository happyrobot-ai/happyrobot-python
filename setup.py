from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

requirements = read_requirements('requirements.txt')

VERSION = '0.2.6'

setup(
    author="Happyrobot",
    author_email='founders@happyrobot.ai',
    name='happyrobot',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="This package lets you interact with Happyrobot directly from Python.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='happyrobot',
    packages=find_packages(include=['happyrobot', 'happyrobot.*']),
    version=VERSION,
    zip_safe=False,
)
