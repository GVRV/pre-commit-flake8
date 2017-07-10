# pre-commit-flake8

Adds pre-commit flake8 support through the simple flake8 command.

See also: https://github.com/pre-commit/pre-commit


## Using pre-commit-isort with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: git://github.com/GVRV/pre-commit-flake8
        sha: ''  # Use the sha you want to point at
        hooks:
        -   id: isort
            args:
            - -c
            - -diff


FAQ
===

Q: Why?
A: Because I couldn't find an existing hook that ran flake8.
