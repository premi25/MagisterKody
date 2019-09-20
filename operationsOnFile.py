# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:37:21 2019

@author: Przemek
"""

import pathlib
#----------------------------------------------------------------
path = pathlib.Path('C:\\Users\Przemek\Desktop')
#----------------------------------------------------------------
#----------------------------------------------------------------
def writeListItemsToCSV(List, filename, delimiter='', filepath=path):
    filename = addExtensionToFilename(filename, '.csv')
    i = 0

    with open (mergePathOfFile(filepath, filename), 'a') as f:
        while (i < len(List)-1):
            f.write(str(List[i])+delimiter)
            f.write('\n')
            i += 1
        f.write(str(List[-1])+delimiter)

def writeItemToCSV(item, filename, delimiter='', filepath=path):
    filename = addExtensionToFilename(filename, '.csv')

    with open (mergePathOfFile(filepath, filename), 'a') as f:
        f.write(str(item)+delimiter)
        f.write('\n')

def addExtensionToFilename(name, extension):
    if not extension in name:
        return name+extension

    return name

def mergePathOfFile(filepath, filename):
    return pathlib.Path(str(filepath)+'\\'+filename)

def listOfFileLines(filepath):
    with open(filepath, 'r') as fp:
        lines = fp.readlines()

    return lines