from pyclustering.cluster.center_initializer import random_center_initializer as rci
from pyclustering.cluster.kmedians import kmedians
from pyclustering.utils.metric import distance_metric

def kmediansRun(sample, k, specMetric):
    initial_medians = rci(sample, k).initialize()
    kmedians_instance = kmedians(sample, initial_medians, metric = distance_metric(specMetric))
	
    kmedians_instance.process()
    clusters = kmedians_instance.get_clusters()
    predicted = kmedians_instance.predict(sample)
    return (clusters, predicted)