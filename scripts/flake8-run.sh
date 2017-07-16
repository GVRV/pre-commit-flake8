#!/bin/sh
git diff HEAD *.py | flake8 --diff
