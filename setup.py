from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

requirements = read_requirements('requirements.txt')

setup(
    author="Happyrobot",
    author_email='founders@happyrobot.ai',
    name='happyrobot_python',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This package lets you interact with Happyrobot directly from Python.",
    # entry_points={
    #     'console_scripts': [
    #         'happyrobot_python=happyrobot_python.cli:main',
    #     ],
    # },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='happyrobot_python',
    packages=find_packages(include=['happyrobot_python', 'happyrobot_python.*']),
    version='0.1.0',
    zip_safe=False,
)
