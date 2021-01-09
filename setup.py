from pathlib import Path

from setuptools import setup, find_packages  # type: ignore[import]

long_description = (Path(__file__).parent / 'README.md').read_text()

setup(
    name='discord-match-logs-uploader',
    version='0.0.1',
    url='https://github.com/PeterJCLaw/discord-match-logs-uploader',
    project_urls={
        'Issue tracker': 'https://github.com/PeterJCLaw/discord-match-logs-uploader/issues',
    },
    description="Uploads match logs to Discord.",
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=['tests']),

    author="Peter Law",
    author_email="PeterJCLaw@gmail.com",

    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ),

    install_requires=(
        'discord.py >=1.6, <2',
    ),
)
