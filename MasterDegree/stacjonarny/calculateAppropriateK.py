from pyclustering.cluster.elbow import elbow
from pyclustering.cluster.center_initializer import random_center_initializer


def calculateAppropriateNumberOfClusters(data, minimum, maximum):
    #elbow_instance = elbow(data, minimum, maximum)
    elbow_instance = elbow(data, minimum, maximum, initializer=random_center_initializer)
    elbow_instance.process()
    return elbow_instance.get_amount()