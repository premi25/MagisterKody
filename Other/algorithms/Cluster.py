from DataPointClass import DataPoint

class Cluster:
    
    oldCenter = DataPoint("")


    def __init__(self, id, center):
        self._id = id
        self._center = center
        self._oldCenter = center
        self._observations = []
    
    def __repr__(self):
       return repr(self.value)
   
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.value[item])
        return [self.value[i] for i in item]
        
    def appendObservation(self, observation):
        point = DataPoint(observation)
        if not point in self._observations:
            self._observations.append(point)

    def updateClusterCenterByMean(self):
        dimension = 0
        dimensionsAmount = len(self._center)
        while dimension < dimensionsAmount:
            sumOfDimension = 0
            for observation in self._observations:
                sumOfDimension += observation.getValue(dimension)
                
            observationsAmount = self.getObservationsAmount()
            mean = round(sumOfDimension/observationsAmount, 5)
            self._center[dimension] = mean
            
            dimension += 1
        
        self.clearstaticOldCenter()

    def clearstaticOldCenter(self):
        self.oldCenter = DataPoint("")

    def assignOldCenter(self, center):
        self.oldCenter = center
        self._oldCenter = DataPoint(self.oldCenter)

    def checkIfClusterChanged(self):
        if self._center == self._oldCenter:
            return False
        return True
                
    def getCenter(self):
        return self._center

            
    def removeObservation(self, observation):
        point = DataPoint(observation)
        if observation in self._observations:
            self._observations.remove(observation)
            
    def getObservations(self):
        return self._observations

    def clearObservations(self):
        self._observations.clear()

    def getObservationsAmount(self):
        return len(self._observations)