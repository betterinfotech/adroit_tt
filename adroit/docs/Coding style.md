# Coding style

- For Python code formatting, we follow [PEP8](https://pep8.org/). 
- This needs to be enforced automatically by configuring Black to run when you save in your IDE

## Naming conventions

In general:

* Classes should be in CamelCase
* Functions and methods should be lower_case_with_underscores
* Local variable names should be  lower_case_with_underscores

## Spelling

For spelling of variable/function/class names use American English spellings
in order to be consistent with the APIs we use e.g. Color not Colour


## Substantive
For more substantive things, the priorities we have [here](Priorities.md) influence
coding style a lot:

- **Very high test coverage** on paths affecting correctness, with a variety of
  testing strategies e.g. regression and unit testing

  
- **Use of assertions** to ensure correctness and help with local reasoning.
  If you are making an assumption that isn’t guaranteed locally, use assert.

- **Extensive use of static typing** to help with correctness and
  refactorings (in ``src``, not required in ``tests``). We run ``pyright src``
  and require zero errors.

  See [these notes](Static typing.md) for more information.


## Comments
- We make extensive use of Docstrings and comments to capture knowledge about requirements.
  Requirements have often not been defined explicitly.

  If the syntax highlighting in your editor de-emphasises comments, as many tend
  to do, that will be **very unhelpful**, and you will miss many things.
