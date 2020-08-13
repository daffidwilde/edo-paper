""" Common functions and parameters amongst the experiments. """

from edo.distributions import Uniform
from sklearn.preprocessing import MinMaxScaler


def scale_dataframe(individual):
    """ Scale the individual's dataframe to the unit square for calculating
    fitness. """

    original = individual.dataframe.copy()
    dataframe = MinMaxScaler().fit_transform(original)

    return dataframe


size = 100
row_limits = [50, 100]
col_limits = [2, 2]
max_iter = 10
best_prop = 0.1
mutation_prob = 0.01

Uniform.param_limits["bounds"] = [0, 1]
distributions = [Uniform]

root = "../data/"
