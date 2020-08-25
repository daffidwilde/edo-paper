This directory contains all of the source code to generate the data used in the
"Evolutionary dataset optimisation" chapter of Henry Wilde's PhD thesis.

The ``environment.yml`` file is used to create a virtual ``conda`` environment.
This environment will ensure that the code herein will reproduce the data and
plots used in the paper exactly. Instructions on how to create, use and
otherwise manage ``conda`` environments can be found at the following link:

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

The file ``common.py`` contains a number of functions and variables that are
used in the remaining files, except for ``__init__.py`` which allows for the
running of the scripts herein.

The source code used in the chapter is otherwise separated by experiment. Each
remaining file is an experiment script to be used with the command-line tool
``edolab`` (included in the virtual environment or pip-installable).

With the conda environment activated, and from this directory, each experiment
should be run as follows:

```
$ PYTHONPATH=. edolab --seeds=10 --cores=<cores> <experiment>.py
```

Here, ``<cores>`` is the number of cores to use and ``<experiment>`` is the name
of the experiment you wish to run.
