# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:50:57 2019

@author: Szatan_Domowy
"""

import random

def randomCenters(howManyData, howManyCenters):
    intialCenters = []
    i = 0
    while i < howManyCenters:
        randomNr = random.randrange(1, howManyData+1)
        if randomNr not in intialCenters:
            intialCenters.append(randomNr)
            i += 1
            
    return intialCenters