#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 13:03:25 2018

@author: valentinarodriguez
"""
import pandas as pd
import numpy as np
from crimeFeatures import Crime

def crimeSeason():
    print("----------------BEGIN CRIME SEASON----------------------------------")
    columns= ['X', 'Y',  "Statute_CrimeCategory","WEAPON","Larceny_Type", "Location_Type","Season"];
    columnsToDrop = ['X','Y']
    dataSeason = pd.read_csv('../../data/crime_prediction/RPD__Part_I_Crime_2011_to_Present_Season.csv')
    dataSeason.columns=[columns]
    crimeFeatures = Crime(dataSeason)
    dataSeason = crimeFeatures.preprocessingCrime(columnsToDrop)
    crimeFeatures.exploration()
    print("----------------END CRIME SEASON----------------------------------")


def crimeOtherFeatures():
    print("----------------BEGIN CRIME OTHER FEATURES----------------------------------")
    columns= ['X', 'Y', 'OBJECTID', 'Reported_Date_Month',"Reported_Time", "Reported_day_of_week_calculated","Reported_Hour_Calculated","Reported_Week_Year_Calculated","Reported_Timestamp","Statute_CrimeCategory","Weapon_Description","Larceny_Type", "Location_Type"]
    columnsToDrop = ['X','Y']
    data = pd.read_csv('../../data/crime_prediction/RPD_crime2011toNow.csv')
    data.columns=[columns]
    crimeFeatures = Crime(data)
    data = crimeFeatures.preprocessingCrime(columnsToDrop)
    crimeFeatures.exploration()
    print("----------------END CRIME OTHER FEATURES----------------------------------")


def crimeOtherFeaturesWithTime():
    print("----------------BEGIN CRIME WITH DAY TIME----------------------------------")
    columns= ['X', 'Y', 'OBJECTID', 'Reported_Date_Month',"Reported_Time", "Reported_day_of_week_calculated","Reported_Hour_Calculated","Reported_Week_Year_Calculated","Reported_Day_Time_Calculated_Numeric","Reported_Timestamp","Statute_CrimeCategory","Weapon_Description","Larceny_Type", "Location_Type"]
    columnsToDrop = ['X','Y']
    data = pd.read_csv('../../data/crime_prediction/RPD_crime2011toNow_withTimeDay.csv')
    data.columns=[columns]
    crimeFeatures = Crime(data)
    data = crimeFeatures.preprocessingCrime(columnsToDrop)
    crimeFeatures.exploration()
    print("data.iloc[:,8]")
    print(data.iloc[:,8])
    print("----------------WEAPON----------------------------------")
    x = np.array(data.iloc[:,9:10].values)# Weapon_Description
    y = np.array(data.iloc[:,8].values)
    crimeFeatures.classification(x,y)
    print("----------------LOCATION TYPE----------------------------------")
    print(data.iloc[:,11:12])
    x = np.array(data.iloc[:,11:12].values)# LOCATION TYPe
    y = np.array(data.iloc[:,8].values)
    crimeFeatures.classification(x,y)
    
    print("----------------TIME OF THE DAY----------------------------------")
    x = np.array(data.iloc[:,6:7].values)# 
    print(data.iloc[:,6:7])
    y = np.array(data.iloc[:,8].values)
    crimeFeatures.classification(x,y)
    
    print("----------------TIME OF THE DAY- WEAPON ----------------------------------")
    x = np.array(data.iloc[:,6:7].values)# 
    print(data.iloc[:,6:7])
    y = np.array(data.iloc[:,8].values)
    crimeFeatures.classification(x,y)
    
    
    print("----------------END CRIME OTHER FEATURES----------------------------------")




def crimeWeatherPrediction():
    print("----------------BEGIN CRIME WITH WEATHER----------------------------------")
    columns= ['x', 'y', 'date', 'crime', 't_low', 't_high', 't_avg', 'DP_avg', 'DP_high','DP_low' , 'h_avg','h_high', 'h_low', 'v_avg', 'v_low', 'v_high', 'w_avg', 'w_low', 'w_high', 'precip', 'events']
    columnsToDrop = ['x','y']
    #for printing the correlation matrix
    #columnsToDrop = ['t_low', 't_high','DP_low', 'DP_high','h_high', 'h_low',  'v_low', 'v_high',  'w_low', 'w_high', ]
    data = pd.read_csv('../../data/crime_prediction/weather-crime.csv')
    data.columns=[columns]
    crimeFeatures = Crime(data)
    data = crimeFeatures.preprocessingWeather(columnsToDrop)
    crimeFeatures.exploration()
    print("----------------END CRIME WITH WEATHER----------------------------------")
   


"""Calling crime predictions for different datasets and features"""
crimeSeason()
crimeOtherFeatures()
crimeOtherFeaturesWithTime()
crimeWeatherPrediction()

