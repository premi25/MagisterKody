# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:43:12 2019

@author: Przemek
"""

#import pathlib
#-------------------------------------------------------------------
from pyclustering.cluster.kmeans import kmeans
from pyclustering.utils.metric import type_metric, distance_metric
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample
#-------------------------------------------------------------------

sample = read_sample(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS)

user_function = lambda point1, point2: point1[0] + point2[0] + 2
metric = distance_metric(type_metric.CHEBYSHEV, func=user_function)

# create K-Means algorithm with specific distance metric
start_centers = [[0.0, 0.1], [0.4, 0.1]];
kmeans_instance = kmeans(sample, start_centers, metric=metric)

# run cluster analysis and obtain results
kmeans_instance.process()
clusters = kmeans_instance.get_clusters()