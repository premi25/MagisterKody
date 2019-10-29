from pyclustering.cluster.center_initializer import random_center_initializer as rci
from pyclustering.cluster.kmeans import kmeans
from pyclustering.utils.metric import distance_metric

def kmeansRun(sample, k, specMetric):
    initial_centers = rci(sample, k).initialize()
    kmeans_instance = kmeans(sample, initial_centers, metric = distance_metric(specMetric))

    kmeans_instance.process()
    clusters = kmeans_instance.get_clusters()
    predicted = kmeans_instance.predict(sample)
    return (clusters, predicted)