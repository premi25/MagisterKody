import pathlib
#-------------------------------------------------------------------
from pyclustering.utils import read_sample
from calculateAppropriateK import calculateAppropriateNumberOfClusters as canoc
#-------------------------------------------------------------------

root = pathlib.Path(r'F:\US_18_19\PracaMag\Data\Research\Other\NewSamples')
fileData100thousand = '100thousand.txt'
fileData75thousand = '75thousand.txt'
fileData50thousand = '50thousand.txt'
fileData20thousand = '20thousand.txt'
fileData10thousand = '10thousand.txt'


def optimalKNumbers(filenameData, filepath, kmin, kmax):
    path = pathlib.Path(str(root)+'\\'+filenameData)
    if path.is_file():
        data = read_sample(path)
        i = 0
    
        while i < 10:
            kClusters, error = canoc(data, kmin, kmax) 
            try:
                with open(filepath, 'a') as f:
                    f.write('kmin: ' + str(kmin) + ' kmax: ' + str(kmax) + ' optimalK: ' + str(kClusters) 
                    + ' errors: ' + str(error)
                    )
                    f.write('\n')
                    return True
            except IOError:
                raise IOError("IOerror")
            
            i += 1
        
optimalKNumbers(fileData100thousand, str(root) + r'\optimalK' + '_1' + '.txt', 1, 316)
optimalKNumbers(fileData75thousand, str(root) + r'\optimalK' + '_2' + '.txt', 1, 273)
optimalKNumbers(fileData50thousand, str(root) + r'\optimalK' + '_3' + '.txt', 1, 223)
optimalKNumbers(fileData20thousand, str(root) + r'\optimalK' + '_4' + '.txt', 1, 141)
optimalKNumbers(fileData10thousand, str(root) + r'\optimalK' + '_5' + '.txt', 1, 100)