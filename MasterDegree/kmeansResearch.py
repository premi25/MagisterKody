import pathlib
#-------------------------------------------------------------------
from meanSilh import meanSilh
#-------------------------------------------------------------------
from kmeansRun import kmeansRun
#-------------------------------------------------------------------
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric
#-------------------------------------------------------------------
from operationsOnFile import writeItemToTxtWithDateTime as witTXT
#-------------------------------------------------------------------
from sklearn.metrics import davies_bouldin_score as dbs
from sklearn.metrics import calinski_harabasz_score as chs

root = pathlib.Path(r'F:\\US_18_19\PracaMag\Data\Research')
fileData100thousand = '100thousand.txt'
fileData75thousand = '75thousand.txt'
fileData50thousand = '50thousand.txt'
fileData20thousand = '20thousand.txt'
fileData10thousand = '10thousand.txt'
fileSilh = 'silhouetteMeans'
fileDBS = 'dbsMeans'
fileCHS = 'chsMeans'
i = 0


def kmeansWithScores(filenameData, filenameSilhMean, nameDBS, nameCHS, kClusters, measure):
    path = pathlib.Path(str(root)+'\\'+filenameData)
    if path.is_file():
        data = read_sample(path)
    
        clusters, predicted = kmeansRun(data, kClusters, measure)

        meanSilhouetteScore = meanSilh(data, clusters)
        witTXT(meanSilhouetteScore, filenameSilhMean, filepath = root, note = filenameData + " k: " + str(kClusters))

        dbsScore = dbs(data, predicted)
        witTXT(dbsScore, nameDBS, filepath = root, note = filenameData + " k: "+ str(kClusters))

        chsScore = chs(data, predicted)
        witTXT(chsScore, nameCHS, filepath = root, note = filenameData + " k: "+ str(kClusters))

while i < 4:
    kmeansWithScores(fileData100thousand, fileSilh, fileDBS, fileCHS, 25, type_metric(i))
    kmeansWithScores(fileData75thousand, fileSilh, fileDBS, fileCHS, 22, type_metric(i))
    kmeansWithScores(fileData50thousand, fileSilh, fileDBS, fileCHS, 20, type_metric(i))
    kmeansWithScores(fileData20thousand, fileSilh, fileDBS, fileCHS, 15, type_metric(i))
    kmeansWithScores(fileData10thousand, fileSilh, fileDBS, fileCHS, 10, type_metric(i))
    if i == 0:
        i += 2
    else:
        i += 1