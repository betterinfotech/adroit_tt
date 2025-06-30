# Priorities

## Correct output

Silently doing the wrong thing is not an option. It is better to
abort a transaction and log the error, than to create wrong output.

## Uptime

We aim for robust system that can absorb shocks (e.g. sudden load) or drop in physical resources (e.g. RAM).

## Clear, usable APIs

The APIs should do what they say they will with no suprises.

## Ability to iterate quickly

## High quality code structure

This exists to support the ability of iterating quickly while not introducing
any serious bugs.

## Ability to debug failures

If we have a runtime failure, it’s critical we have logs etc for diagnosis. 

## Performance

The tool meets requirements as specified in the SLA.

## Less important things:
- Beautiful and polished interface
