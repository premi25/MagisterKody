# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:39:34 2019

@author: Przemek
"""

from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.utils import read_sample
from pyclustering.utils.metric import distance_metric, type_metric
import pathlib

path = pathlib.Path('C:\\Users\Przemek\Desktop\sample1.txt')

# Load list of points for cluster analysis.
sample = read_sample(path)

# create metric that will be used for clustering
metric = distance_metric(type_metric.MINKOWSKI, degree=2)

# Calculate 2 initial centers using K-Means++ method.
initial_centers = kmeans_plusplus_initializer(sample, 1).initialize()

# Perform cluster analysis using K-Means algorithm with initial centers.
kmeans_instance = kmeans(sample, initial_centers, metric=metric)

# Run cluster analysis and obtain results.
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()
final_centers = kmeans_instance.get_centers()

# Visualize obtained results
kmeans_visualizer.show_clusters(sample, clusters, final_centers)