# coding: utf-8

import numpy as np 
from numpy import *
import matplotlib.pyplot as plt

# 測試資料集 -- 二維 list
dataSet = [
    [-0.017612, 14.053064],
    [-1.395634, 4.662541],
    [-0.752157, 6.538620],
    [-1.322371, 7.152853],
    [0.423363, 11.054677],
    [0.406704, 7.067335],
    [0.667394, 12.741452],
    [-2.460150, 6.866805],
    [0.569411, 9.548755],
    [-0.026632, 10.427743],
    [0.850433, 6.920344],
    [1.347183, 13.175500],
    [1.176813, 3.167020],
    [-1.781871, 9.097953]
]

# change list to matrix

dataMat = mat(dataSet).T
plt.scatter(array(dataMat[0]),array(dataMat[1]),c='red')

# print linear picture

# get a linear dataset
x = np.linspace(-2,2,100)

# build a linear formula
y = 2.8*x + 9

plt.plot(x,y)
plt.show()
