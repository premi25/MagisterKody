# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:39:08 2019

@author: Przemek
"""

from pyclustering.cluster.kmeans import kmeans
from pyclustering.utils.metric import type_metric, distance_metric



user_function = lambda point1, point2: point1[0] + point2[0] + 2
metric = distance_metric(type_metric.CHEBYSHEV, func=user_function)
sample = read_sample()

# create K-Means algorithm with specific distance metric
start_centers = [[4.7, 5.9], [5.7, 6.5]];
kmeans_instance = kmeans(sample, start_centers, metric=metric)

# run cluster analysis and obtain results
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()