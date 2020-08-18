""" Experiment script for k-means with silhouette and discounting corr. """

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import common


def fitness(individual, n_clusters=3, n_seeds=5):
    """ Cluster the data into `n_clusters` parts across `n_seeds` runs and
    return the maximum difference between the silhouette and absolute
    correlation coefficient. """

    dataframe = common.scale_dataframe(individual)
    corr = abs(individual.dataframe.corr().iloc[0, 1])
    differences = []
    for seed in range(n_seeds):
        km = KMeans(n_clusters, random_state=seed).fit(dataframe)
        differences.append(silhouette_score(dataframe, km.labels_) - corr)

    best = max(differences)
    return best


size = common.size
row_limits = common.row_limits
col_limits = common.col_limits
max_iter = common.max_iter
best_prop = common.best_prop
mutation_prob = common.mutation_prob
maximise = True

distributions = common.distributions

root = common.root

__all__ = [
    "size",
    "row_limits",
    "col_limits",
    "max_iter",
    "best_prop",
    "mutation_prob",
    "distributions",
]
