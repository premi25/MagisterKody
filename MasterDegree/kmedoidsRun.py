from randomCenters import randomCenters
#-------------------------------------------------------------------
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.utils.metric import distance_metric

def kmedoidsRun(sample, k, specMetric):
    initial_medoids = randomCenters(len(sample), k)
    kmedoids_instance = kmedoids(sample, initial_medoids, metric = distance_metric(specMetric))
	
    kmedoids_instance.process()
    clusters = kmedoids_instance.get_clusters()
    predicted = kmedoids_instance.predict(sample)
    return (clusters, predicted)