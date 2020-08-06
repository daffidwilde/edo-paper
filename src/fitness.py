""" Fitness functions for the experiments. """

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def inertia(individual, nclusters=3, nseeds=5):
    """ Return the final inertia when clustering the individual dataset into
    ``nclusters`` parts across ``nseeds`` trials. """

    inertias = []
    for seed in range(nseeds):
        km = KMeans(nclusters, random_state=seed).fit(individual.dataframe)
        inertias.append(km.inertia_)

    return min(inertias)


def silhouette(individual, nclusters=3, nseeds=5):
    """ Return the silhouette coefficient of the clustering of the dataset into
    ``nclusters`` parts across ``nseeds`` trials. """

    silhouettes = []
    for seed in range(nseeds):
        km = KMeans(nclusters, random_state=seed).fit(individual.dataframe)
        silhouette = silhouette_score(individual.dataframe, km.labels_)
        silhouettes.append(silhouette)

    return min(silhouettes)


def scaled_inertia(individual, nclusters=3, nseeds=5):
    """ Scale the dataset and then calculate fitness with ``inertia``. """

    original_dataframe = individual.dataframe.copy()
    individual.dataframe = StandardScaler().fit_transform(individual.dataframe)
    fit = inertia(individual, nclusters, nseeds)

    individual.dataframe = original_dataframe

    return fit


def scaled_silhouette(individual, nclusters=3, nseeds=5):
    """ Scale the dataset and then calculate fitness with ``silhouette``. """

    original_dataframe = individual.dataframe.copy()
    individual.dataframe = StandardScaler().fit_transform(individual.dataframe)
    fit = silhouette(individual, nclusters, nseeds)

    individual.dataframe = original_dataframe

    return fit
