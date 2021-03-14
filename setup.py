import setuptools


setuptools.setup(
    name="argparse-best-practice",
    version="0.1.3",
    license='MIT',
    author="oneofthezombies",
    author_email="hunhoekim@gmail.com",
    description="python argparse best practice.",
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url="https://github.com/oneofthezombies/argparse-best-practice",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
