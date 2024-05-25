from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
setup(
    name="blocks_duo_ss_five",
    version="0.0.1",
    description="smartscape blocks-duo player package",
    author="Team five",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "ss_five=ss_player.main:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]
)