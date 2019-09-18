# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:43:12 2019

@author: Przemek
"""

from pyclustering.cluster.kmeans import kmeans
from pyclustering.utils.metric import type_metric, distance_metric
import pathlib

path = pathlib.Path('C:\\Users\Przemek\Desktop\sample.txt')
content = ""
if path.is_file():
    in_file = open(path, 'r')
    content = in_file.read()

user_function = lambda point1, point2: point1[0] + point2[0] + 2
metric = distance_metric(type_metric.CHEBYSHEV, func=user_function)
sample = read_sample()

# create K-Means algorithm with specific distance metric
start_centers = [[0.0, 0.1], [0.4, 0.1]];
kmeans_instance = kmeans(sample, start_centers, metric=metric)

# run cluster analysis and obtain results
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()