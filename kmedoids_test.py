# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:57:07 2019

@author: Przemek
"""

import pathlib
#-------------------------------------------------------------------
import numpy as np
import random
#-------------------------------------------------------------------

from pyclustering.cluster.elbow import elbow
from pyclustering.cluster.kmedoids import kmedoids
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
filenameSilhouette = 'silhouetteMedoids.csv'
filenameSilhouetteMean = 'silhouetteMedoids_mean.csv'
filenameDBS = 'dbsMedoids.csv'
filenameCHS = 'chsMedoids.csv'
k = 10
k_min, k_max = 1, 15
metric = distance_metric(type_metric.EUCLIDEAN)

def initialSetOfMedoids(k_clusters, points_amount):
    medoidsToInit = []
    while len(medoidsToInit) < k_clusters:
        number = random.randrange(0, points_amount)
        if not number in medoidsToInit:
            medoidsToInit.append(number)

    return medoidsToInit


def kmedoidsWithScore(nameData, nameSilhouetteMean, nameDBS, nameCHS, k_clusters, measure, kmin, kmax):
    data = read_sample(str(root)+'\\'+nameData)

    initial_medoids = initialSetOfMedoids(k_clusters, len(data))

    kmedoids_instance = kmedoids(data, initial_medoids)
    kmedoids_instance.process()
    clusters = kmedoids_instance.get_clusters()
    predicted = kmedoids_instance.predict(data)

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

kmedoidsWithScore(filenameData, filenameSilhouetteMean, filenameDBS, filenameCHS, k, metric, k_min, k_max)