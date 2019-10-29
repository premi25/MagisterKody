import random

def randomCenters(howManyData, howManyCenters):
    intialCenters = []
    i = 0
    while i < howManyCenters:
        randomNr = random.randrange(0, howManyData)
        if randomNr not in intialCenters:
            intialCenters.append(randomNr)
            i += 1
            
    return intialCenters