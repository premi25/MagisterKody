import pathlib
#-------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------
from calculateAppropriateK import calculateAppropriateNumberOfClusters as canoc
#-------------------------------------------------------------------
from pyclustering.cluster.center_initializer import random_center_initializer  as rci
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.silhouette import silhouette
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric
#-------------------------------------------------------------------
from operationsOnFile import writeItemToCSV as witCSV
from operationsOnFile import writeItemToTxtWithDateTime as witTXT
#-------------------------------------------------------------------
from sklearn.metrics import davies_bouldin_score as dbs
from sklearn.metrics import calinski_harabasz_score as chs

root = pathlib.Path('F:\\US_18_19\PracaMag\Data\Research')
fileData100thousand = 'dataForResearch100thousand.txt'
fileData75thousand = 'dataForResearch75thousand.txt'
fileData50thousand = 'dataForResearch50thousand.txt'
fileData20thousand = 'dataForResearch20thousand.txt'
fileData10thousand = 'dataForResearch10thousand.txt'
fileSilhMean = 'silhouette_mean.csv'
fileDBS = 'dbsMedoids.csv'
fileCHS = 'chsMedoids.csv'
metricResearch = distance_metric(type_metric.EUCLIDEAN)
kminimum = 1
kmaximum = 10


def kmedoidsWithScores(nameData, nameSilhouetteMean, nameDBS, nameCHS, k_clusters, measure, kmin, kmax):
	data = read_sample(str(root)+'\\'+filenameData)
    
    kClusters = canoc(data, kmin, kmax)
    
    initial_medoids = rci(data, kClusters).initialize()
    kmedoids_instance = kmedoids(data, initial_medoids, metric = metricResearch)
	
    kmedoids_instance.process()
    clusters = kmedoids_instance.get_clusters()
    predicted = kmedoids_instance.predict(data)

	silhouetteScore = silhouette(data, clusters).process().get_score()
    meanSilhouetteScore = np.mean(silhouetteScore)
    witTXT(meanSilhouetteScore, filenameSilhMean, filepath = root, note = filenameData + " k: "+ str(kClusters))

    dbsScore = dbs(data, predicted)
    witTXT(dbsScore, filenameDBS, filepath = root, note = filenameData + " k: "+ str(kClusters))
	
    chsScore = chs(data, predicted)
    witTXT(chsScore, filenameCHS, filepath = root, note = filenameData + " k: "+ str(kClusters))

kmedoidsWithScores(fileData100thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
kmedoidsWithScores(fileData75thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
kmedoidsWithScores(fileData50thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
kmedoidsWithScores(fileData20thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)
kmedoidsWithScores(fileData10thousand, fileSilhMean, fileDBS, fileCHS, kminimum, kmaximum)