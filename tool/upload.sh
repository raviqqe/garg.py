#!/bin/sh

for file in $(find test -type f)
do
  python3 $file > /dev/null
done &&

git clean -dfX &&
python3 setup.py sdist bdist_wheel &&
twine upload dist/*
