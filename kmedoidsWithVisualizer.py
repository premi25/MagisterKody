# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:27:00 2019

@author: Przemek
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:39:34 2019

@author: Przemek
"""

from pyclustering.cluster.kmedoids import kmedoids
#from pyclustering.cluster import cluster_visualizer
from pyclustering.utils import read_sample
from pyclustering.utils.metric import distance_metric, type_metric
import pathlib

path = pathlib.Path('C:\\Users\Przemek\Desktop\sample1.txt')

# Load list of points for cluster analysis.
sample = read_sample(path)

# create metric that will be used for clustering
metric = distance_metric(type_metric.EUCLIDEAN)

# Set random initial medoids.
initial_medoids = [1, 3, 4]
 
# create K-Medoids algorithm with specific distance metric
kmedoids_instance = kmedoids(sample, initial_medoids, metric=metric)
 
# run cluster analysis and obtain results
kmedoids_instance.process()
clusters = kmedoids_instance.get_clusters()
 
# Show allocated clusters.
print(clusters)
 
"""# Display clusters.
visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, sample)
visualizer.show()"""