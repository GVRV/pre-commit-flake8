#!/bin/sh
git diff HEAD | flake8 --diff
