import sys
from setuptools import setup

if sys.version_info < (3, 6):
    raise Exception("Only Python 3.6 and above is supported.")


install_requires = []

setup(
    name="gym_40k",
    version="0.0.1",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: POSIX",
    ],
    packages=["gym_40k"],
    zip_safe=False,
    install_requires=["gym>=0,<1", "numpy>=1,<2", "six>=1,<2"],
    extras_require={},
)