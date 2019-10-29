from pyclustering.cluster.center_initializer import random_center_initializer
from pyclustering.cluster.elbow import elbow

def calculateAppropriateNumberOfClusters(data, minimum, maximum, specInit = random_center_initializer):
    elbow_instance = elbow(data, minimum, maximum, initializer=specInit)
    elbow_instance.process()
    return (elbow_instance.get_amount(), elbow_instance.get_wce())