#!/bin/bash

rm -rf dist;
rm -rf earcut.egg*;
python setup.py sdist; 
python -m twine upload dist/*;