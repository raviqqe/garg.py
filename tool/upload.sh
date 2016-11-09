#!/bin/sh

python3 test/simple.py arg1 &&

git clean -dfX &&
python3 setup.py sdist bdist_wheel &&
twine upload dist/*
