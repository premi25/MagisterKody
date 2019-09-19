# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:55:25 2019

@author: Przemek
"""

import pathlib
from checkIfListContainsDuplicatedItems import listOfItemsSplitted as lois
from checkIfListContainsDuplicatedItems import removeEmptyItems as rei
from checkIfListContainsDuplicatedItems import removeObjectsWithMissingValues as rowmv
from checkIfListContainsDuplicatedItems import removeStringsWithMissingValues as rswmv
from inlineForSetTupleVSLongVersionWithFors import longVersion as lv
from operationsOnFile import listOfFileLines as lofl
from operationsOnFile import writeListItemsToCSV as wlitCSV

path = pathlib.Path('F:\Studies_18_19\PracaMag\Dane\household_power_consumption.txt')
filenameToWrite = 'hpc_DataWithoutMissingItems.csv'
listOfListsWithoutEndLine = []
listOfListsWithoutEmptyItems = []
#k = 100000
#i = 0

fileContent = lofl(path)
fileContent = rswmv(fileContent)
for line in fileContent:
    listOfListsWithoutEndLine.append(lois(line, '\n'))
for item in listOfListsWithoutEndLine:
    listOfListsWithoutEmptyItems.append(rei(item))
cleanListOfLists = lv(listOfListsWithoutEmptyItems)
for i in cleanListOfLists:
    wlitCSV(i, filenameToWrite)