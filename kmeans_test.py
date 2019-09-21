# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:09:16 2019

@author: Przemek
"""

import pathlib
#-------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------
#from pyclustering.cluster import cluster_visualizer_multidim
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer as kppi
from pyclustering.cluster.elbow import elbow
from pyclustering.cluster.kmeans import kmeans
from pyclustering.cluster.silhouette import silhouette
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric
#-------------------------------------------------------------------
from operationsOnFile import writeListItemsToCSV as wlitCSV
from operationsOnFile import writeItemToCSV as witCSV
#-------------------------------------------------------------------
from sklearn.metrics import davies_bouldin_score as dbs
from sklearn.metrics import calinski_harabasz_score as chs

root = pathlib.Path('F:\\US_18_19\PracaMag\Data')
filenameData = 'dataReadyForClusteringWork.txt'
filenameSilhouette = 'silhouette1.csv'
filenameSilhouetteMean = 'silhouette_mean.csv'
filenameDBS = 'dbs.csv'
filenameCHS = 'chs.csv'
#filename
k = 10
k_min, k_max = 1, 15
metric = distance_metric(type_metric.EUCLIDEAN)

def kmeansWithScores(nameData, nameSilhouetteMean, nameDBS, nameCHS, k_clusters, measure, kmin, kmax):
    data = read_sample(str(root)+'\\'+nameData)

    initial_centers = kppi(data, k_clusters).initialize()
    kmeans_instance = kmeans(data, initial_centers, metric = measure)

    kmeans_instance.process()
    clusters = kmeans_instance.get_clusters()
    predicted = kmeans_instance.predict(data)

#    final_centers = kmeans_instance.get_centers()
#kv.show_clusters(data, clusters, final_centers) #too many dimensions

#visualizer = cluster_visualizer_multidim()
#visualizer.append_clusters(clusters, data)
#visualizer.show(pair_filter=[[0, 7]])

#from sklearn.cluster import KMeans
#kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
    silhouetteScore = silhouette(data, clusters).process().get_score()
    meanSilhouetteScore = np.mean(silhouetteScore)
    wlitCSV(silhouetteScore, filenameSilhouette, '', root)
    witCSV(meanSilhouetteScore, nameSilhouetteMean, '', root)

    dbsScore = dbs(data, predicted)
    witCSV(dbsScore, nameDBS, '', root)

    chsScore = chs(data, predicted)
    witCSV(chsScore, nameCHS, '', root)

    elbow_instance = elbow(data, kmin, kmax)
    elbow_instance.process()
    amount_clusters = elbow_instance.get_amount()  # most probable amount of clusters
    wce = elbow_instance.get_wce()

    print ("amount_cluster" + str(amount_clusters))
    print ("wce" + str(wce))

kmeansWithScores(filenameData, filenameSilhouetteMean, filenameDBS, filenameCHS, k, metric, k_min, k_max)