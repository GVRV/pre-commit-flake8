#!/bin/sh
git diff --cached **/*.py | flake8 --diff
