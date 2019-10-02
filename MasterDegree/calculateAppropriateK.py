from pyclustering.cluster.elbow import elbow


def calculateAppropriateNumberOfClusters(data, minimum, maximum):
    elbow_instance = elbow(data, minimum, maximum)
    elbow_instance.process()
    return elbow_instance.get_amount()