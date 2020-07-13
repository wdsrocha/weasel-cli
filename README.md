<p align="center"><a href="https://pypi.org/project/weasel-cli/" target="_blank" rel="noopener noreferrer"><img width="100" src="https://raw.githubusercontent.com/wdsrocha/weasel-cli/master/logo.svg" alt="Weasel CLI logo"></a></p>

<p align="center">
  <a href="https://github.com/wdsrocha/weasel-cli/blob/master/LICENSE"><img src="https://img.shields.io/github/license/wdsrocha/weasel-cli?color=blue" alt="license"></a>
  <a href="https://pypi.org/project/weasel-cli/"><img src="https://img.shields.io/pypi/v/weasel-cli" alt="version"></a>
  <a href="https://github.com/wdsrocha/weasel-cli/actions?query=workflow%3Abuild"><img src="https://img.shields.io/github/workflow/status/wdsrocha/weasel-cli/build" alt="build"></a>
  <a href="https://github.com/wdsrocha/weasel-cli/blob/master/CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="prs"></a>
</p>

<h1 align="center">Dawkins' Weasel CLI</h1>

Simple implementation of the classic [weasel program](https://en.wikipedia.org/wiki/Weasel_program).

![demo](https://raw.githubusercontent.com/wdsrocha/weasel-cli/master/cli_demo.png)

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

## Contributing

See [CONTRIBUTING.md](https://github.com/wdsrocha/weasel-cli/blob/master/CONTRIBUTING.md) file for more information.

## License

This project is licensed under the terms of the MIT license - see the `LICENSE` file for details.

---

Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).