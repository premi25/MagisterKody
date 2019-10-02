# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:52:42 2019

@author: Przemek
"""

import pathlib
#-------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer as kppi
from pyclustering.cluster.elbow import elbow
from pyclustering.cluster.kmedians import kmedians
from pyclustering.cluster.silhouette import silhouette
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric
#-------------------------------------------------------------------
#from operationsOnFile import writeListItemsToCSV as wlitCSV
#from operationsOnFile import writeItemToCSV as witCSV
#-------------------------------------------------------------------
from sklearn.metrics import davies_bouldin_score as dbs
from sklearn.metrics import calinski_harabasz_score as chs

root = pathlib.Path('F:\\US_18_19\PracaMag\Data')
filenameData = 'dataReadyForClusteringWork.txt'
filenameSilhouette = 'silhouetteMedians.csv'
filenameSilhouetteMean = 'silhouetteMedians_mean.csv'
filenameDBS = 'dbsMedians.csv'
filenameCHS = 'chsMedians.csv'
k = 10
k_min, k_max = 1, 15
metric = distance_metric(type_metric.EUCLIDEAN)


def kmediansWithScore(nameData, nameSilhouetteMean, nameDBS, nameCHS, k_clusters, measure, kmin, kmax):
    data = read_sample(str(root)+'\\'+nameData)

    initial_medians = kppi(data, k_clusters).initialize()
    kmedians_instance = kmedians(data, initial_medians)
    kmedians_instance.process()

    clusters = kmedians_instance.get_clusters()
#    final_medians = kmedians_instance.get_medians()

    predicted = kmedians_instance.predict(data)

    silhouetteScore = silhouette(data, clusters).process().get_score()
    meanSilhouetteScore = np.mean(silhouetteScore)
    #wlitCSV(silhouetteScore, filenameSilhouette, '', root)
    #witCSV(meanSilhouetteScore, nameSilhouetteMean, '', root)

    dbsScore = dbs(data, predicted)
    #witCSV(dbsScore, nameDBS, '', root)

    chsScore = chs(data, predicted)
    #witCSV(chsScore, nameCHS, '', root)

    elbow_instance = elbow(data, kmin, kmax)
    elbow_instance.process()
    amount_clusters = elbow_instance.get_amount()  # most probable amount of clusters
    wce = elbow_instance.get_wce()


kmediansWithScore(filenameData, filenameSilhouetteMean, filenameDBS, filenameCHS, k, metric, k_min, k_max)
