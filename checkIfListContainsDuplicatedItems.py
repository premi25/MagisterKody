# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:20:16 2019

@author: Przemek
"""

import pathlib
#----------------------------------------------------------------------
#----------------------------------------------------------------------
path = pathlib.Path('C:\\Users\Przemek\Desktop\household_power_consumption.txt')
#----------------------------------------------------------------------
#----------------------------------------------------------------------
def listOfItemsSplitted(item,character):
    workList = str(item).split(character)

    return workList

def removeEmpty(List):
    test = list(filter(None, List))
    return test

def listOfUniqueItems(ListOfLists):
    return list(list(innerList) for innerList in set(tuple(innerList) for innerList in ListOfLists))

def removeObjectsWithMissingValues(ListOfLists, character='?'):
    listOfNonmissingValuesObjects = []
    for i in ListOfLists:
        if not character in i:
            listOfNonmissingValuesObjects.append(i)
            
    return listOfNonmissingValuesObjects

def removeStringsWithMissingValues(List, character='?'):
    listOfNonmissingValuesObjects = []
    for i in List:
        if not character in i:
            listOfNonmissingValuesObjects.append(i)
            
    return listOfNonmissingValuesObjects

def removeEmptyItems(List):
    listWithoutEmptyItems = []
    for item in List:
        if not item == '':
            listWithoutEmptyItems.append(item)

    return listWithoutEmptyItems

def transformListToDictionary(listToTransformation):
    objectsWithoutDelimitersAndMissingValues = []
    objectsWithoutEmptyItems = []
    for item in listToTransformation:
        objectsWithoutDelimitersAndMissingValues.append(listOfItemsSplitted(item, "\n"))

    for item in objectsWithoutDelimitersAndMissingValues:
        objectsWithoutEmptyItems.append(removeEmpty(item))

    objectsWithoutDelimitersAndMissingValues = clearListAndAssignParameter(objectsWithoutEmptyItems, objectsWithoutDelimitersAndMissingValues)

    listToTransformation = clearListAndAssignParameter(objectsWithoutDelimitersAndMissingValues, listToTransformation)
    
    for item in listToTransformation:
        objectsWithoutDelimitersAndMissingValues.append(listOfItemsSplitted(item, ';'))
    
    listToTransformation = clearListAndAssignParameter(objectsWithoutDelimitersAndMissingValues, listToTransformation)

    for item in objectsWithoutDelimitersAndMissingValues:
        objectsWithoutDelimitersAndMissingValues.append(listOfItemsSplitted(item, ']'))

        objectsWithoutDelimitersAndMissingValues = removeEmpty(objectsWithoutDelimitersAndMissingValues)

    objectsWithoutDelimitersAndMissingValues = removeObjectsWithMissingValues(objectsWithoutDelimitersAndMissingValues)

def clearListAndAssignParameter(listToClear, listToAssign):
    listToAssign = list(listToClear)
    listToClear.clear()
    return listToAssign