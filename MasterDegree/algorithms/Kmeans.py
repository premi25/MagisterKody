import random
import dataPoint
import CallMetric
import Cluster

centers = [dataPoint()]
clusters = [Cluster()]
dataPoints = [dataPoint()]
breakLoop = False

def calculate(point1, point2, metricID):
    dataPoints = [point1, point2]
    callMetric = CallMetric(metricID)
    return callMetric.callSpecifiedMetric(dataPoints)
            
def setRandomCenters(dataPoints, k):
    i = 0
    while i < k:
        randomCenter = random.choice(dataPoints)
        if not randomCenter in centers:
            centers.append(randomCenter)
            i += 1
            
def filldataPointsBase(data):  
    point = dataPoint()
    for observation in data:
        point.value = observation
        dataPoints.append(point)

def getAllCenters():
    for cluster in clusters:
        centers.append(cluster.getCenter())
    return centers
        
def getClusterByCenter(center):
    for cluster in clusters:
        if cluster._center == center:
            return cluster
    
    return Cluster()
      
def getClosestCluster(observation, metricId):
    minimum = float("inf")
    closestCluster = Cluster()
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
 
    setRandomCenters(dataPoints, k)   
            
    for iteration in iterations:
        for observation in dataPoints:
            changedClusters = [Cluster()]
            closestCluster = getClosestCluster(observation, metricId)
            closestCluster.appendObservation(observation)
            closestCluster.assignOldCenter()
            closestCluster.updateClusterCenterByMean()
        
            if not closestCluster.checkIfClusterChanged():
                changedClusters.append(closestCluster)
        
            clustersButclosestCluster = list(clusters)
            clustersButclosestCluster.remove(closestCluster)
        
            for cluster in clustersButclosestCluster:
                if observation in cluster.getObservations:
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
            
    return clusters