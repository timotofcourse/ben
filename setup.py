from setuptools import find_packages, setup

setup(
    name="timot-ben",
    version="0.0.1",
    description="My personal download module with my syntax",
    package_dir={"":"ben"},
    packages=find_packages(where="ben"),
    long_description="My own personal download module to use in my other projects",
    url="https://github.com/timotofcourse/ben",
    author="filmabemtv2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT LICENSE",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "rich"],
    extra_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.12",
)