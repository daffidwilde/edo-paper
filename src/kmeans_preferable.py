""" Experiment script for k-means preferred to DBSCAN w.r.t. silhouette. """

from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score

import common


def fitness(individual, n_clusters=3, eps=0.14, min_samples=5, n_seeds=5):
    """ Cluster the data into `n_clusters` parts with k-means across `n_seeds`
    runs, and with DBSCAN using `eps` and `min_samples`. Find the difference in
    their silhouette scores and return the largest. """

    dataframe = common.scale_dataframe(individual)

    db = DBSCAN(eps=eps, min_samples=min_samples).fit(dataframe)
    outlier_mask = db.labels_ == -1
    labels = db.labels_[~outlier_mask]
    if len(set(labels)) > 1:
        data = dataframe[~outlier_mask, :]
        db_score = silhouette_score(data, labels)
    else:
        db_score = None

    differences = []
    for seed in range(n_seeds):
        km = KMeans(n_clusters, random_state=seed).fit(dataframe)
        km_score = silhouette_score(dataframe, km.labels_)

        if db_score is not None:
            differences.append(km_score - db_score)
        else:
            differences.append(-3)

    return max(differences)


size = common.size
row_limits = common.row_limits
col_limits = common.col_limits
max_iter = common.max_iter
best_prop = common.best_prop
mutation_prob = common.mutation_prob
maximise = True

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
