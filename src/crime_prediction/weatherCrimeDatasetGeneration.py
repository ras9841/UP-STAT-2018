#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
It will generate a new dataset with the crime and weather information according to the same date.
Created on Wed Mar 28 13:52:11 2018
https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/pairwise.py
@author: valentinarodriguez
"""
from sklearn.metrics.pairwise import euclidean_distances
import mysql.connector
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Crime(object):
    def __init__(self, objectId, x, y,date, category ):
        self.objectId = objectId
        self.x = x
        self.y = y
        self.date = date
        self.category = category

crimeList = []


class Weather(object):
 def __init__(self,   t_low, t_high, t_avg, DP_avg, DP_high,DP_low , h_avg,h_high, h_low, v_avg, v_low, v_high, w_avg, w_low, w_high, precip, events):
       self.DP_avg = DP_avg 
       self.DP_high=DP_high
       self.DP_low= DP_low
       self.h_avg= h_avg
       self.h_high=h_high 
       self.h_low= h_low 
       self.t_avg= t_avg
       self.t_high=t_high 
       self.t_low= t_low 
       self.v_avg= v_avg 
       self.v_low =v_low
       self.v_high = v_high 
       self.w_avg= w_avg
       self.w_low = w_low
       self.w_high= w_high
       self.precip  = precip 
       self.events = events
weatherList = []

class WeatherCrime(object):
    def __init__(self,x, y, date, category, t_low, t_high, t_avg, DP_avg, DP_high,DP_low , h_avg,h_high, h_low, v_avg, v_low, v_high, w_avg, w_low, w_high, precip, events):
        self.x = x
        self.y = y
        self.category = category
        self.date = date
        self.DP_avg = DP_avg 
        self.DP_high=DP_high
        self.DP_low= DP_low
        self.h_avg= h_avg
        self.h_high=h_high 
        self.h_low= h_low 
        self.v_avg= v_avg 
        self.v_low =v_low
        self.v_high = v_high 
        self.w_avg= w_avg
        self.w_low = w_low
        self.w_high= w_high
        self.precip  = precip 
        self.events = events
        self.t_avg= t_avg
        self.t_high=t_high 
        self.t_low= t_low 
       
    
weatherCrimeList = []


try:
  cnx = mysql.connector.connect(user='root', host='127.0.0.1',
                                database='UPSTAT')
  
  cursor = cnx.cursor()
  query = ("SELECT crime.x as x, crime.y as y, DATE_FORMAT(crime.Reported_Timestamp,'%Y-%m-%d') as date, crime.objectid, Statute_CrimeCategory as category " + 
           "FROM UPSTAT.RPD__Part_I_Crime_2011_to_Present crime WHERE DATE_FORMAT(crime.Reported_Timestamp,'%Y-%m-%d') >= '2017-01-01' and y is not null and x  is not null " +
           "order by date, X,Y;")
  cursor.execute(query)

  for (x, y, date, objectid, category) in cursor:
      if int(category) < 5:
         category = 'VC'
      else:
         category = 'NVC'

      crimeList.append(Crime(objectid, x, y, date, category)) 
  
  cursor.close()

  for crime in crimeList:
        arrayCrime=[[crime.x, crime.y]]
        queryW = ("SELECT DATE_FORMAT(weather.date, '%Y-%m-%d') as date, t_low as t_low , t_high as t_high, t_avg, DP_avg as DP_avg, DP_high as DP_high,DP_low as DP_low, h_avg as h_avg,h_high, h_low, v_avg, v_low, v_high, w_avg, w_low, w_high, precip, events " + 
           "FROM UPSTAT.dataset_weather weather " +
           "where DATE_FORMAT(weather.date, '%Y-%m-%d') = '" + crime.date +
           "' order by date")
        cursorW = cnx.cursor()
        cursorW.execute(queryW)
        distancePrev = 10000000000000
        weather = None
        for (date, t_low, t_high, t_avg, DP_avg, DP_high,DP_low , h_avg,h_high, h_low, v_avg, v_low, v_high, w_avg, w_low, w_high, precip, events) in cursorW: 
            weather = Weather(t_low, t_high, t_avg, DP_avg, DP_high,DP_low , h_avg,h_high, h_low, v_avg, v_low, v_high, w_avg, w_low, w_high, precip, events)
            weatherCrimeList.append(WeatherCrime(crime.x, crime.y, crime.date, crime.category, weather.t_low,  weather.t_high,  weather.t_avg,  weather.DP_avg,  weather.DP_high,DP_low ,  weather.h_avg, weather.h_high,  weather.h_low,  weather.v_avg,  weather.v_low,  weather.v_high,  weather.w_avg,  weather.w_low, weather.w_high, weather.precip, weather.events))   
        
        
  cursorW.close()
except mysql.connector.Error as err:
    print(err)
else:
  cnx.close()
  

  with open('weather-crime.csv', 'w') as wcfile:
      fieldnames = ['x', 'y', 'date', 'category', 't_low', 't_high', 't_avg', 'DP_avg', 'DP_high','DP_low' , 'h_avg','h_high', 'h_low', 'v_avg', 'v_low', 'v_high', 'w_avg', 'w_low', 'w_high', 'precip', 'events']
      writer = csv.DictWriter(wcfile, fieldnames=fieldnames,  delimiter = ',')
      writer.writeheader()
      for weatherCrime in weatherCrimeList:
          writer.writerow({'x': weatherCrime.x, 'y': weatherCrime.y, 'date': weatherCrime.date, 'category': weatherCrime.category, 't_low': weatherCrime.t_low, 't_high':  weatherCrime.t_high,  't_avg': weatherCrime.t_avg, 'DP_avg':  weatherCrime.DP_avg,  'DP_high': weatherCrime.DP_high, 'DP_low': weatherCrime.DP_low ,  'h_avg': weatherCrime.h_avg, 'h_high': weatherCrime.h_high,  'h_low': weatherCrime.h_low, 'v_avg':  weatherCrime.v_avg,  'v_low': weatherCrime.v_low,  'v_high': weatherCrime.v_high,  'w_avg': weatherCrime.w_avg,  'w_low': weatherCrime.w_low, 'w_high': weatherCrime.w_high, 'precip': weatherCrime.precip, 'events': weatherCrime.events})
