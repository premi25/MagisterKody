# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pathlib

path1 = pathlib.Path('F:\\US_18_19\PracaMag\Data\household_power_consumption.txt')
path2 = pathlib.Path('F:\\US_18_19\PracaMag\Data\hpc_100000_semicolon.csv')

data1 = []
data2 = []
counter = 0

with open(path1, 'r') as fp:
    data1 = fp.readlines()

with open(path2, 'r') as fp:
    data2 = fp.readlines()

for i in data2:
    if i in data1:
        counter += 1
    print(counter)


