import pathlib
#-------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------
from calculateAppropriateK import calculateAppropriateNumberOfClusters as canoc
#-------------------------------------------------------------------
from pyclustering.cluster.center_initializer import random_center_initializer  as rci
from pyclustering.cluster.kmeans import kmeans
from pyclustering.cluster.silhouette import silhouette
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric
#-------------------------------------------------------------------
#from operationsOnFile import writeListItemsToCSV as wlitCSV
from operationsOnFile import writeItemToCSV as witCSV
#-------------------------------------------------------------------
from sklearn.metrics import davies_bouldin_score as dbs
from sklearn.metrics import calinski_harabasz_score as chs

root = pathlib.Path('F:\\US_18_19\PracaMag\Data\Research')
fileData100thousand = 'dataForResearch100thousand.txt'
fileData75thousand = 'dataForResearch75thousand.txt'
fileData50thousand = 'dataForResearch50thousand.txt'
fileData20thousand = 'dataForResearch20thousand.txt'
fileData10thousand = 'dataForResearch10thousand.txt'
#fileSilh = 'silhouetteMeans.csv'
fileSilhMean = 'silhouetteMeans_mean.csv'
fileDBS = 'dbsMeans.csv'
fileCHS = 'chsMeans.csv'
metricResearch = distance_metric(type_metric.EUCLIDEAN)
kminimum = 1
kmaximum = 10


def kmeansWithScores(filenameData, filenameSilhMean, filenameDBS, filenameCHS, kmin, kmax):
    data = read_sample(str(root)+'\\'+filenameData)
    
    kClusters = canoc(data, kmin, kmax)
    
    initial_centers = rci(data, kClusters).initialize()
    kmeans_instance = kmeans(data, initial_centers, metric = metricResearch)

    kmeans_instance.process()
    clusters = kmeans_instance.get_clusters()
    predicted = kmeans_instance.predict(data)

    silhouetteScore = silhouette(data, clusters).process().get_score()
    meanSilhouetteScore = np.mean(silhouetteScore)
    #wlitCSV(silhouetteScore, filenameSilh, '', root)
    witCSV(meanSilhouetteScore, filenameSilhMean, '', root)

    dbsScore = dbs(data, predicted)
    witCSV(dbsScore, filenameDBS, '', root)

    chsScore = chs(data, predicted)
    witCSV(chsScore, filenameCHS, '', root)

#kmeansWithScores(fileData100thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
#kmeansWithScores(fileData75thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
#kmeansWithScores(fileData50thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
#kmeansWithScores(fileData20thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
#kmeansWithScores(fileData10thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)