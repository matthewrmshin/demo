# Python Demo Project by Matt

A demo Conda Python project with bells and whistles.

## Run Project in a Conda Environment

Get and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Check out this project and change directory to its root. Run:

```sh
# Install
conda env create -n demo  # Choose another name if `demo` already in use
conda activate demo
python3 setup.py install test

# Lint
flake8

# Build docs
make -C docs/ html

# Say hello
demo_hello
```
