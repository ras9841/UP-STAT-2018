#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 13:07:13 2018

@author: valentinarodriguez
"""
import preprocessingCrimeData
import preprocessingWeatherData
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc
import sklearn.metrics as metrics
import sklearn as skl
from mlxtend.evaluate import confusion_matrix
import sklearn.linear_model as linear_model

class Crime:
    
    __slots__ = ("data")
    
    def __init__( self, data):
        self.data = data
    
    def preprocessingCrime(self, columnsToDrop):
        data = preprocessingCrimeData.convertingCategorizedDataToNumerical(self.data)
        data = preprocessingCrimeData.dataCleaning(data, columnsToDrop)
        print("Printing data")
        print(data)
        self.data = data
        return data
        
    def preprocessingWeather(self, columnsToDrop):
        data = preprocessingWeatherData.dataCleaning(self.data, columnsToDrop)
        print("Printing data")
        print(data)
        self.data = data
        return data

    def exploration(self):
        print("Printing correlations Matrix")
        corr = self.data.corr()
        print(corr)
        sns.heatmap(corr, square=True)
        plt.show()
        
     
    def classification(self,x, y):
         """Sampling"""
         sss = StratifiedShuffleSplit(n_splits=3, test_size=0.3, random_state=0)
         x_train= [] 
         x_test= []
         y_train= []
         y_test = []
         for train_index, test_index in sss.split(x, y):
             x_train, x_test = x[train_index], x[test_index]
             y_train, y_test = y[train_index], y[test_index]

         "----------------------------------LOGISTIC REGRESSION ----------------------------------"
         classifier_lr = LogisticRegression()
         classifier_lr.fit(x_train, y_train)
         y_predict_logistic = classifier_lr.predict(x_test)
        
         cm_logistic = metrics.confusion_matrix(y_test, y_predict_logistic)  
         print(cm_logistic)
        
         acc_logistic = accuracy_score(y_test,y_predict_logistic)
         print("Accuracy Logistic Regression" + str(acc_logistic))
         f1_score_logistic = skl.metrics.f1_score(y_test, y_predict_logistic, average='macro')
         print ("F1-score Logistic Regression: %f" % f1_score_logistic)
         precision_lr = precision_score(y_test, y_predict_logistic, pos_label=3, average='macro')
        
         print("Precision Logistic Regression " + str(precision_lr))
         recall_lr = recall_score(y_test, y_predict_logistic, pos_label=3, average='macro')
        
         print("Recall Logistic Regression " + str(recall_lr))
        
         "----------------------------------LINEAR SVN ----------------------------------"
         classifier_svc = svm.LinearSVC()
         classifier_svc.fit(x_train, y_train)
         y_pred_svc_linear = classifier_svc.predict(x_test)
         cm_svc_linear = confusion_matrix(y_test,y_pred_svc_linear)
         print(cm_svc_linear)
        
         acc_svc_linear = accuracy_score(y_test,y_pred_svc_linear)
         print("Accuracy SVN" + str(acc_svc_linear))
         f1_score_svn = skl.metrics.f1_score(y_test, y_pred_svc_linear, average='macro')
         print ("F1-score Linear SVN: %f" % f1_score_svn)
         precision_svn = precision_score(y_test, y_pred_svc_linear, pos_label=3, average='macro')
        
         print("Precision Linear SVN " + str(precision_svn))
         recall_svn = recall_score(y_test, y_pred_svc_linear, pos_label=3, average='macro')
        
         print("Recall Linear SVN " + str(recall_svn))
         "----------------------------------PERCEPTRON ----------------------------------"
         clf_perceptron = Perceptron(n_iter=2, shuffle=False)
         clf_perceptron.fit(x_train, y_train)
         y_pred_perceptron =  clf_perceptron.predict(x_test)
         cm_perceptron = confusion_matrix(y_test,y_pred_perceptron)
         print(cm_perceptron)
         acc_perceptron = accuracy_score(y_test,y_pred_perceptron)
         print("Accuracy Perceptron" + str(acc_perceptron))
         f1_score_perceptron = skl.metrics.f1_score(y_test, y_pred_perceptron, average='macro')
         print ("F1-score Perceptron: %f" % f1_score_perceptron)
         precision_perceptron = precision_score(y_test, y_pred_perceptron, pos_label=3, average='macro')
        
         print("Precision Perceptron " + str(precision_perceptron))
        
         recall_perceptron = recall_score(y_test, y_pred_perceptron, pos_label=3, average='macro')
        
         print("Recall Perceptron " + str(recall_perceptron))
         """----------------------------------LINEAR REGRESSION ----------------------------------"""
         regression = linear_model.LinearRegression()
         regression.fit(x_train, y_train)
         y_pred_regression = regression.predict(x_test)
         cm_regression = confusion_matrix(y_test,y_pred_regression)
         print(cm_regression)
         #score = regression.score(x_test, y_test)
         print('Coefficients for Linear Regression: \n', regression.coef_)

         plt.figure()
         plt.plot(regression.coef_, color='navy', linestyle='--')
         plt.title('Coefficients for Linear Regression')
         plt.show()

