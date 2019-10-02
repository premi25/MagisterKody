from chebyshev_metric import calculateChebyshev
from euclidean_metric import calculateEuclidean
from manhattan_metric import calculateManhattan


class CallMetric:
    def __init__(self, value):
       self.value = value
    
    def __repr__(self):
       return repr(self.value)
   
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.value[item])
        return [self.value[i] for i in item]
    
    def callSpecifiedMetric(self, dataPoints):
        if (self.value == 1):
            return calculateManhattan(dataPoints)
        elif (self.value == 2):
            return calculateEuclidean(dataPoints)
        elif (self.value == 3):
            return calculateChebyshev(dataPoints)