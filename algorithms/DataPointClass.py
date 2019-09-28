class DataPoint:
   def __init__(self, value):
       self.value = value
    
   def __repr__(self):
       return repr(self.value)
   
   def getWidth(self):
       return len(self.value)
   
   def __getitem__(self, item):
    if isinstance(item, (int, slice)):
        return self.__class__(self.value[item])
    return [self.value[i] for i in item]