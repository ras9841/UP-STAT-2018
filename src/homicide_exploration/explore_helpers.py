import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def yPerX_numeric(xlabel, x, ylabel, y):
    uniqueX = x.unique()
    data = { ux : 0 for ux in uniqueX }
    for ux in uniqueX:
        xLocs = x.isin([ux])
        yc = y[xLocs].sum()
        data[ux] += yc
    plt.figure()
    plt.bar(uniqueX, list(data.values()), edgecolor="k")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def yPerX_cat(xlabel, x, ylabel, y):
    uniqueX = x.unique()
    data = { ux : 0 for ux in uniqueX }
    for ux in uniqueX:
        xLocs = x.isin([ux])
        yc = y[xLocs].size
        data[ux] += yc
    plt.figure()
    plt.bar(uniqueX, list(data.values()), edgecolor="k")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
