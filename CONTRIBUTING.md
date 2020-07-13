# Contributing Guide

## 🚧 Local development

To start developing, execute the following steps:

1. Install the [Poetry](https://python-poetry.org/) package manager;
2. Run `poetry install` to install dependencies.

Now you can test the local CLI with `poetry run weasel`. This does accept options, so running `poetry run weasel --help` or something like that, works just fine 👌.

Make sure to upgrade the project version with `poetry version` after finishing your changes. 

## 🚀 Testing your changes

In order to test your changes in a production environment, using [TestPyPI](https://test.pypi.org/) is recommended.

1. Create an account on [TestPyPI](https://test.pypi.org/), if you don't have one;
2. Run `poetry config repositories.test-pypi https://test.pypi.org/legacy/`;
3. Publish your version to TestPyPI with `poetry publish -r test-pypi --build`.
4. Test the CLI with `pip install --index-url https://test.pypi.org/legacy/ name-of-your-project`

You may need to change the project name and version for this to work (due to how TestPyPI works), but just remember to undo this before submitting your Pull Request.

If everything is okay, now it's time to submit the Pull Request and wait for the reviewers! ✨