import math

# accepts list of DataPoint objects
def calculateManhattan(listOfPoints):
    distanceSum = 0;
    i = 0
    if len(listOfPoints) == 1:
        return 0
    elif len(listOfPoints) == 2:
        point0 = listOfPoints[0]
        point1 = listOfPoints[1]
        dimensions = point0.getWidth()
        while i < dimensions :
            distanceSum += math.fabs(float(str(point0[i]))-float(str(point1[i])))
            i += 1
        return round(distanceSum,5)
    else:
        raise ValueError("List's length should be in range from 1 to 2!")