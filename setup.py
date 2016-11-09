#!/usr/bin/env python

import setuptools
import sys


if not sys.version_info[0] >= 3:
  exit("Sorry, Python's version must be later than 3.")


def main():
  with open("README.rst") as f:
    readme = f.read()

  setuptools.setup(
    name="garg",
    version="0.0.1",
    description="Global argparse parser",
    long_description=readme,
    license="Public Domain",
    author="Yota Toyama",
    author_email="raviqqe@gmail.com",
    url="http://github.com/raviqqe/garg.py/",
    py_modules=["garg"],
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: Public Domain",
      "Programming Language :: Python :: 3",
    ],
  )


if __name__ == "__main__":
  main()
