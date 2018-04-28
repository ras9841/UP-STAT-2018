#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:09:02 2018

@author: valentinarodriguez
"""



def dataCleaning(data, columnsToDrop):
    data= data.replace(to_replace="NVC",value=-1)
    data= data.replace(to_replace="VC",value=+1)
    print("dataCleaning")
    print(data)
    return data


