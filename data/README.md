DATA
====

This directory contains all of the data generated as part of the paper
"Evolutionary Dataset Optimisation: learning algorithm quality through
evolution".

Each tarball corresponds to a different experiment in the case study presented
in the work. Once uncompressed, each experiment directory contains five trial
directories named by the random seed that was used to generate the data therein
that is structured as follows:

- ``data.tar.gz``: a tarball of the data associated with the trial.
- ``summary``: a directory containing a summary of the data in ``data.tar.gz``,
  i.e.:
    - ``main.csv``: a CSV detailing the index, dimensions, memory consumption,
      generation and fitness of every individual in the trial.
    - ``max``: a directory containing the dataset and metadata of the individual
      with the highest fitness score in the trial.
    - ``median``: a directory containing the dataset and metadata of the
      individual with the closest-to-median fitness score in the trial.
    - ``min``: a directory containing the dataset and metadata of the individual
      with the lowest fitness score in the trial.
