import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyevacalor",
    version="0.0.6",
    author="Frederic Van Linthoudt",
    author_email="frederic.van.linthoudt@gmail.com",
    description="pyevacalor provides controlling Eva Calor heating devices connected via the IOT Agua platform of Micronova",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fredericvl/pyevacalor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
