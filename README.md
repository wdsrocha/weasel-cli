# Dawkins' Weasel Program

[![license](https://img.shields.io/github/license/wdsrocha/weasel-cli?color=blue)](https://github.com/wdsrocha/weasel-cli/blob/master/LICENSE)
[![version](https://img.shields.io/pypi/v/weasel-cli)](https://pypi.org/project/weasel-cli/)
[![build](https://img.shields.io/github/workflow/status/wdsrocha/weasel-cli/build)](https://github.com/wdsrocha/weasel-cli/actions?query=workflow%3Abuild)
[![prs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/wdsrocha/weasel-cli/blob/master/CONTRIBUTING.md)

Simple implementation of the classic [weasel program](https://en.wikipedia.org/wiki/Weasel_program).

![demo](https://raw.githubusercontent.com/wdsrocha/weasel-cli/master/demo.png)

## About

Although the weasel simulation really works, I'm using this project mostly to test things like CLI development, Github Actions, PyPI deployment, etc.

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
