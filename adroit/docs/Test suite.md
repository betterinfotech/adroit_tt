# Test suite

The test suite is run using [pytest](https://docs.pytest.org/en/stable/)

  "pytest tests/"

Pytest has many features and extensive documentation that will enable you to use
it much more effectively - for example by only running a subset of the tests.

Please see this [pytest cheatsheet](https://cheatography.com/nanditha/cheat-sheets/pytest/)


## Test strategy

We use a variety of different kinds of automated tests, from unit tests to
regression tests. 


## Regression tests
We use regression tests to make sure a change does not inadvertently break code elsewhere.

## Static type checks

We also require pyright checks to pass.

"pyright src"

## Lint checks

We also require ruff checks to pass.

"ruff check ."
