""" Experiment script for k-means with inertia. """

from sklearn.cluster import KMeans

import common


def fitness(individual, n_clusters=3, n_seeds=5):
    """ Cluster the data into `n_clusters` parts across `n_seeds` runs and
    return the minimum inertia. Record labelling (for post-run analysis.) """

    dataframe = common.scale_dataframe(individual)
    inertias, labels = [], []
    for seed in range(n_seeds):
        km = KMeans(n_clusters, random_state=seed).fit(dataframe)
        inertias.append(km.inertia_)
        labels.append(km.labels_)

    best = min(inertias)
    individual.labels = labels[inertias.index(best)]

    return best


size = common.size
row_limits = common.row_limits
col_limits = common.col_limits
max_iter = common.max_iter
best_prop = common.best_prop
mutation_prob = common.mutation_prob

distributions = common.distributions


__all__ = [
    "size",
    "row_limits",
    "col_limits",
    "max_iter",
    "best_prop",
    "mutation_prob",
    "distributions",
]
