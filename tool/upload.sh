#!/bin/sh

for file in $(find test -type f)
do
  python3 $file > /dev/null
done &&

python3 setup.py sdist bdist_wheel &&
twine upload dist/*
