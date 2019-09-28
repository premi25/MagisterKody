class DataPoint:
    
    _values = []
    
    def __init__(self, value):
       self._values = value
    
    def __repr__(self):
       return repr(self.value)
   
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.__class__(self.value[item])
        return [self.value[i] for i in item]
    
    def getValue(self, dimensionId):
        return self._values[dimensionId]
    
    def getDimensionsAmount(self):
        return len(self._values)