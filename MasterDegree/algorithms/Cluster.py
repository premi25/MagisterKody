import dataPoint

class Cluster:
    _center = dataPoint()
    _oldCenter = dataPoint()
    _observations = [dataPoint()]
    
    def __init__(self, _center, observations):
       self._center = _center
       self._observations = observations
    
    def __repr__(self):
       return repr(self.value)
   
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.value[item])
        return [self.value[i] for i in item]
    
    def updateClusterCenterByMean(self):
        sumOfDimension = 0
        dimension = 0
        dimensionsAmount = self._center.getDimensionsAmount()
        while dimension < dimensionsAmount:
            for observation in self._observations:
                sumOfDimension += observation.getValue()
                
            mean = sumOfDimension/dimensionsAmount
            self._center[dimension] = mean
            
            dimension += 1

    def assignOldCenter(self):
        self._oldCenter = self._center
                
    def checkIfClusterChanged(self):
        if self._center == self._oldCenter:
            return False
        return True
                
    def getCenter(self):
        return self._center
    
    def appendObservation(self, observation):
        if not observation in self._observations:
            self._observations.append(observation)
            
    def removeObservation(self, observation):
        if observation in self._observations:
            self._observations.remove(observation)
            
    def getObservations(self):
        return self._observations
        