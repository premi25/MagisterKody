import numpy as np
#-------------------------------------------------------------------
from pyclustering.cluster.silhouette import silhouette

def meanSilh(data, clusters):
    silhouetteScore = silhouette(data, clusters).process().get_score()
    return np.mean(silhouetteScore)