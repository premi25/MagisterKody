# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:13:53 2019

@author: Przemek
"""

#listaList = [[1,2],[1,2],[1,3]]
#listaTuple = [(1,2),(1,2),(1,3)]
#tupleTuple = ((1,2),(1,2),(1,3))

listWithoutDuplicates = []
listUnique = []

def getListWithoutDuplicates(ListOfList):
    for i in set(tuple(x) for x in ListOfList):
        listWithoutDuplicates.append(i)

    for j in listWithoutDuplicates:
        listUnique.append(list(j))

    return listUnique #unique_data

#unique = list(list(x) for x in a) #unique_data

#unique_dat =  list(list(x) for x in set(tuple(x) for x in listaList))

#unique_data = [list(x) for x in set(tuple(x) for x in listaList)]