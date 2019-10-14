import pathlib
#-------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------
#from calculateAppropriateK import calculateAppropriateNumberOfClusters as canoc
#-------------------------------------------------------------------
from pyclustering.cluster.center_initializer import random_center_initializer as rci
from pyclustering.cluster.kmeans import kmeans
from pyclustering.cluster.silhouette import silhouette
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric
#-------------------------------------------------------------------
from operationsOnFile import writeItemToTxtWithDateTime as witTXT
#-------------------------------------------------------------------
from sklearn.metrics import davies_bouldin_score as dbs
from sklearn.metrics import calinski_harabasz_score as chs

root = pathlib.Path(r'C:\Users\Szatan_Domowy\Desktop\Praca_mag\Dane\Research')
fileData100thousand = '100thousand.txt'
fileData75thousand = '75thousand.txt'
fileData50thousand = '50thousand.txt'
fileData20thousand = '20thousand.txt'
fileData10thousand = '10thousand.txt'
fileSilhMean = 'silhouetteMeans'
fileDBS = 'dbsMeans'
fileCHS = 'chsMeans'
metricResearch = distance_metric(type_metric.CHEBYSHEV)
#kminimum = 1
#kmaximum = 10


#def kmeansWithScores(filenameData, filenameSilhMean, filenameDBS, filenameCHS, kmin, kmax):
def kmeansWithScores(filenameData, filenameSilhMean, filenameDBS, filenameCHS, kClusters):
    data = read_sample(str(root)+'\\'+filenameData)
    
    #kClusters = canoc(data, kmin, kmax)
    
    initial_centers = rci(data, kClusters).initialize()
    kmeans_instance = kmeans(data, initial_centers, metric = metricResearch)

    kmeans_instance.process()
    clusters = kmeans_instance.get_clusters()
    predicted = kmeans_instance.predict(data)

    silhouetteScore = silhouette(data, clusters).process().get_score()
    meanSilhouetteScore = np.mean(silhouetteScore)
    witTXT(meanSilhouetteScore, filenameSilhMean, filepath=root, note = 'k: ' + str(kClusters))

    dbsScore = dbs(data, predicted)
    witTXT(dbsScore, filenameDBS, filepath = root, note = 'k: ' + str(kClusters))

    chsScore = chs(data, predicted)
    witTXT(chsScore, filenameCHS, filepath = root, note = 'k: ' + str(kClusters))

kmeansWithScores(fileData100thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 5)
kmeansWithScores(fileData75thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 5)
kmeansWithScores(fileData50thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 4)
kmeansWithScores(fileData20thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 4)
kmeansWithScores(fileData10thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 4)