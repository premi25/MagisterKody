import pathlib
#-------------------------------------------------------------------
import numpy as np
#-------------------------------------------------------------------
#from calculateAppropriateK import calculateAppropriateNumberOfClusters as canoc
#-------------------------------------------------------------------
from randomCenters import randomCenters
from pyclustering.cluster.kmedoids import kmedoids
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
fileSilhMean = 'silhouetteMedoids'
fileDBS = 'dbsMedoids'
fileCHS = 'chsMedoids'
metricResearch = distance_metric(type_metric.MANHATTAN)
#kminimum = 1
#kmaximum = 10


def kmedoidsWithScores(filenameData, filenameSilhMean, filenameDBS, filenameCHS, kClusters):
	data = read_sample(str(root)+'\\'+filenameData)
	
	#kClusters = canoc(data, kmin, kmax)
	
	initial_medoids = randomCenters(len(data), kClusters)
	kmedoids_instance = kmedoids(data, initial_medoids, metric = metricResearch)
	
	kmedoids_instance.process()
	clusters = kmedoids_instance.get_clusters()
	predicted = kmedoids_instance.predict(data)
	
	silhouetteScore = silhouette(data, clusters).process().get_score()
	meanSilhouetteScore = np.mean(silhouetteScore)
	witTXT(meanSilhouetteScore, filenameSilhMean, filepath = root, note='k: ' + str(kClusters))
	
	dbsScore = dbs(data, predicted)
	witTXT(dbsScore, filenameDBS, filepath = root, note='k: ' + str(kClusters))
	
	chsScore = chs(data, predicted)
	witTXT(chsScore, filenameCHS, filepath = root, note='k: ' + str(kClusters))

kmedoidsWithScores(fileData100thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 223)
kmedoidsWithScores(fileData75thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 192)
kmedoidsWithScores(fileData50thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 154)
kmedoidsWithScores(fileData20thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 99)
kmedoidsWithScores(fileData10thousand, fileSilhMean, fileDBS, fileCHS, kClusters = 66)