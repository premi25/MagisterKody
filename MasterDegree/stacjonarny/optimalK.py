import pathlib
#-------------------------------------------------------------------
from pyclustering.utils import read_sample
from pyclustering.utils.metric import type_metric, distance_metric
from calculateAppropriateK import calculateAppropriateNumberOfClusters as canoc
#-------------------------------------------------------------------

root = pathlib.Path(r'C:\Users\Szatan_Domowy\Desktop\Praca_mag\Dane\Research')
fileData100thousand = '100thousand.txt'
fileData75thousand = '75thousand.txt'
fileData50thousand = '50thousand.txt'
fileData20thousand = '20thousand.txt'
fileData10thousand = '10thousand.txt'
fileSilhMean = 'silhouetteMedoids'
fileDBS = 'dbsMedoids'
fileCHS = 'chsMedoids'
metricResearch = distance_metric(type_metric.EUCLIDEAN)


def optimalKNumbers(filenameData, filepath, kmin, kmax):
    data = read_sample(str(root)+'\\'+filenameData)
    kClusters = canoc(data, kmin, kmax)
    
    try:
        with open(filepath, 'a') as f:
            f.write('kmin: '+str(kmin)+' kmax: '+str(kmax)+' optimalK: '+str(kClusters))
            f.write('\n')
        return True
    except IOError:
        raise IOError("Writing error")
        
optimalKNumbers(fileData100thousand, str(root)+r'\optimalK.txt', 218, 228)
optimalKNumbers(fileData75thousand, str(root)+r'\optimalK.txt', 188, 198)
optimalKNumbers(fileData50thousand, str(root)+r'\optimalK.txt', 153, 163)
optimalKNumbers(fileData20thousand, str(root)+r'\optimalK.txt', 95, 105)
optimalKNumbers(fileData10thousand, str(root)+r'\optimalK.txt', 65, 75)