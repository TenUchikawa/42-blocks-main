from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
setup(
    name="blocks_duo_ss",
    version="0.0.1",
    description="smartscape blocks-duo package",
    author="Yoshitomi",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "start_blocksduo=blocks_duo.GameMaster:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ]
)