import pathlib
#-------------------------------------------------------------------
from pyclustering.utils import read_sample
from Kmeans import Kmeans


root = pathlib.Path('F:\\US_18_19\PracaMag\Data')
filenameData = 'dataReadyForClusteringWork.txt'


clusters = Kmeans((read_sample(str(root)+'\\'+filenameData)), 5, 2, 5)