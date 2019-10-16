SOURCE CODE
===========

This directory contains all of the source code to generate the data and plots
used in the paper "Evolutionary Dataset Optimisation: learning algorithm quality
through evolution".

At the top level of this directory is an ``environment.yml`` file used to create
a virtual ``conda`` environment. This environment will ensure that the code
herein will reproduce the data and plots used in the paper exactly. Instructions
on how to create, use and otherwise manage conda environments can be found at
the following link:

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Each directory within this directory corresponds to a different experiment from
the case study presented in the work. Each experiment directory contains two
files:

- ``data.py``: a script used to generate the data for a given trial (indicated
  by an integer seed parameter at runtime). Uses 0 by default.
- ``plots.py``: a script used to generate and save the plots for the experiment.
  Uses trial 0 by default. Assumes that the data is available in the directory
  structure defined in ``data.py``. For instance, for trial 0 of
  ``kmeans_over_dbscan``, this script looks for data in
  ``../data/kmeans_over_dbscan/0/data/``.
