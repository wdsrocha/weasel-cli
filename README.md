# Dawkins' Weasel Program

Simple implementation of the classic [weasel program](https://en.wikipedia.org/wiki/Weasel_program).

![demo](https://raw.githubusercontent.com/wdsrocha/weasel-cli/master/demo.png)

## Installation

`pip install weasel-cli`

## Usage

```
$ weasel --help
Usage: weasel [OPTIONS]

  Simulate Dawkins' weasel experiment

Options:
  -t, --target TEXT               [default: METHINKS IT IS LIKE A WEASEL]
  -p, --population-size INTEGER RANGE
                                  [default: 100]
  -r, --mutation-rate FLOAT RANGE
                                  [default: 0.05]
  --color / --no-color            Uses ANSI colors when reporting generation
                                  results  [default: True]

  --help                          Show this message and exit.
```

## License

This project is licensed under the terms of the MIT license - see the `LICENSE` file for details.
