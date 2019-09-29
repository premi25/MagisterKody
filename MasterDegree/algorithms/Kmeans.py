import random
from DataPointClass import DataPoint
from CallMetricClass import CallMetric
from Cluster import Cluster

breakLoop = False
centers = []
clusters = []
clustersToReturn = []
dataPoints = []

def calculate(point1, point2, metricID):
    dataPoints = [point1, point2]
    callMetric = CallMetric(metricID)
    return callMetric.callSpecifiedMetric(dataPoints)

def createClustersWithCenters():
    i = 0
    for center in centers:
        cluster = Cluster(i, center)
        cluster.appendObservation(center)
        clusters.append(cluster)
        i += 1

def convertDataPointsClustersToClusters():
    i = 0
    for cluster in clusters:
        for observation in cluster._observations:
            clustersToReturn[i].append(observation)
        i += 1
            
def filldataPointsBase(data): 
    for observation in data:
        dataPoints.append(observation)

def getAllCenters():
    centers = []
    for cluster in clusters:
        centers.append(cluster.getCenter())
    return centers
        
def getClusterByCenter(center):
    for cluster in clusters:
        if cluster._center == center:
            return cluster
    
    return cluster
        
def setRandomCenters(dataPoints, k):
    i = 0
    while i < k:
        randomCenter = random.choice(dataPoints)
        if not randomCenter in centers:
            centers.append(randomCenter)
            i += 1
      
def getClosestCluster(observation, metricId):
    minimum = float("inf")
    centers = getAllCenters()
    for center in centers:
        result = calculate(observation, center, metricId)
        if minimum > result:
            minimum = result
            closestCluster = getClusterByCenter(center)
            
    return closestCluster

def Kmeans(data, k, metricId, iterations):
    
    if (len(data) < k):
        raise ValueError("Length of data is smaller than k")
 
    filldataPointsBase(data)
    setRandomCenters(dataPoints, k)
    createClustersWithCenters()
            
    for iteration in range(iterations):
        for observation in dataPoints:
            changedClusters = []
            closestCluster = getClosestCluster(observation, metricId)
            closestCluster.appendObservation(observation)
            closestCluster.assignOldCenter(closestCluster._center)
            closestCluster.updateClusterCenterByMean()
        
            if closestCluster.checkIfClusterChanged():
                changedClusters.append(closestCluster)
        
            clustersButclosestCluster = list(clusters)
            clustersButclosestCluster.remove(closestCluster)
        
            for cluster in clustersButclosestCluster:
                if observation in cluster.getObservations():
                    cluster.removeObservation(observation)
                cluster.assignOldCenter()
                cluster.updateClusterCenterByMean()
            
                if not cluster.checkIfClusterChanged():
                    changedClusters.append(cluster)
            
            if len(changedClusters) == 0:
                breakLoop = True;
                break
        
        if breakLoop:
            break
        
    convertDataPointsClustersToClusters()
            
    return clusters