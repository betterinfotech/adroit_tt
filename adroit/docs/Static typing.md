# Static typing

In this project, as part of our [coding style](Coding style.md) we lean heavily on static type checks.

## Purposes

Static type checking provides us with a number of very helpful things:

- Checking of many type-related errors, both:

  - As you code
  - As a linting step before you merge code

  The big point is to take problems that would be errors at runtime, and make
  them visible as errors **much earlier**, before you even attempt to run the
  code.

## Type checker

We run static type checks currently with pyright.
Try to integrate pyright checks into your
IDE, as it can provide many helpful checks as you are coding
that will catch bugs early.
