from setuptools import setup


setup(
    name='pre_commit_dummy_flake8_package',
    version='0.0.1',
    install_requires=[
        'flake8==3.3.0',
        'flake8-builtins==0.4',
        'flake8-comprehensions==1.4.1',
        'flake8-isort==2.2.1',
        'flake8-polyfill==1.0.1',
        'flake8-string-format==0.2.3'
    ],
)
