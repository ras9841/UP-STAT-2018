#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:09:02 2018

@author: valentinarodriguez
"""
import seaborn as sns
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import svm
import matplotlib as mat
import matplotlib.pyplot as plt
from mlxtend.evaluate import confusion_matrix 
from mlxtend.evaluate import plot_confusion_matrix
import sklearn.cross_validation as cross_validation
from sklearn.cross_validation import train_test_split
import sklearn.metrics as metrics
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc
import sklearn.preprocessing as preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import LogisticRegression
import sklearn as skl
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc
from ggplot import *
from sklearn.linear_model import Perceptron
import sklearn.linear_model as linear_model
import sklearn.preprocessing as preprocessing

dataWC = pd.read_csv('weather-crime-lastdetailedCrime2.csv')
#dataWC = pd.read_csv('weather-crime-data-reduced2-temp.csv')
dataWC.columns=['x', 'y', 'date', 'crime', 't_low', 't_high', 't_avg', 'DP_avg', 'DP_high','DP_low' , 'h_avg','h_high', 'h_low', 'v_avg', 'v_low', 'v_high', 'w_avg', 'w_low', 'w_high', 'precip', 'events']

#dataWC = dataWC.drop(['WT11','WT01','WT03','WT04','WT06','WT09'], axis=1)#no data
#TODO - revise source code.

dataWC = dataWC.drop(['x','y'], axis=1)
new_dataTraining = dataWC


# plot correlation matrix

def convert_categorical_to_number(df):
    dfCopy = df.copy()
    result = {}
    for element in dfCopy.columns:
        if dfCopy.dtypes[element] == np.object:
             if element != "date":
                 result[element] = preprocessing.LabelEncoder()
                 dfCopy[element] = result[element].fit_transform(dfCopy[element])     
    return dfCopy, result

"----------------------------------PLOT ROC ----------------------------------"

def roc(y_test, y_pred):
    y_test = y_test.astype(int)
    y_pred = y_pred.astype(int)
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    auc_var = metrics.auc(fpr,tpr)
    print("ACU : " + str(auc_var))
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='red', lw=lw, label='ROC curve (area = %0.2f)' %auc_var)
    plt.plot([0, 1], [0, 1], color='g', lw=lw, linestyle='--')
    plt.xlabel('False Positive')
    plt.ylabel('True Positive')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.title('ROC Curve')
    plt.legend(loc="lower right")
    plt.show()



print("new_dataTrainingn------------1")
print (new_dataTraining)
    
print("new_dataTrainingn------------2")
print (new_dataTraining)
new_dataTraining= new_dataTraining.replace(to_replace="NVC",value=-1)
new_dataTraining= new_dataTraining.replace(to_replace="VC",value=+1)
#new_dataTraining= new_dataTraining.replace(to_replace="T",value=0.15)
new_dataTraining = new_dataTraining.fillna(0)
#new_dataTraining, results = convert_categorical_to_number(new_dataTraining)
"""new_dataTraining= new_dataTraining.replace(to_replace="Rain",value=1)
new_dataTraining= new_dataTraining.replace(to_replace="Snow",value=20)
new_dataTraining= new_dataTraining.replace(to_replace="Fog",value=3)
new_dataTraining= new_dataTraining.replace(to_replace="Thurnderstorm",value=11)
new_dataTraining= new_dataTraining.replace(to_replace="Fog , Rain , Hail , Thunderstorm",value=10)
new_dataTraining= new_dataTraining.replace(to_replace="Fog , Rain , Thunderstorm",value=15)
new_dataTraining= new_dataTraining.replace(to_replace="Fog , Rain , Snow",value=24)
new_dataTraining= new_dataTraining.replace(to_replace="Fog , Snow , Thunderstorm",value=34)
new_dataTraining= new_dataTraining.replace(to_replace="Fog , Rain",value=4)
new_dataTraining= new_dataTraining.replace(to_replace="Rain , Snow, Thunderstorm",value=34)
new_dataTraining= new_dataTraining.replace(to_replace="Rain , Thunderstorm",value=12)
new_dataTraining= new_dataTraining.replace(to_replace="Snow , Rain",value=21)


"""



print("new_dataTrainingn------------3")
print(new_dataTraining["events"])

print("xval")
corr = new_dataTraining.corr()
print(corr)
sns.heatmap(corr, square=True)
plt.show()
print("xval2")


cm = new_dataTraining.corr()
fig = plt.figure()

ax = fig.add_subplot(111)
cax = ax.matshow(cm)

plt.colorbar(cax)
ticks = np.arange(0,11,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(new_dataTraining.columns)
ax.set_yticklabels(new_dataTraining.columns)
print("aval")
plt.show()
print("bval2")

data = new_dataTraining[['t_high']].as_matrix()
type_label = np.where(new_dataTraining['crime']== +1,+1,-1)
print("crime")
print(type_label)
x = np.array(data)
y = np.array(type_label)



def GridClassifier(x, y):
    C_range = np.logspace(-2, 10, 13)
    gamma_range = np.logspace(-9, 3, 13)
    param_grid = dict(gamma=gamma_range, C=C_range)
    cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
    grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv)
    grid.fit(x, y)
    
    print("The best parameters are %s with a score of %0.2f"
          % (grid.best_params_, grid.best_score_))
    
    # Now we need to fit a classifier for all parameters in the 2d version
    # (we use a smaller set of parameters here because it takes a while to train)
    


def svnClassifier(x,y):
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.30, stratify=y)
    # Set the parameters by cross-validation
   
    clf = svm.SVC(kernel='linear', probability=True)
    clf.fit(x_train, y_train)
    print("x_train")
    print(x_train)
    y_pred_svc = clf.predict(x_test)
    print("y_pred_svc" + str(y_pred_svc))
  #  print("probability " + str(clf.predict_proba))
    #confusion matrix for SVM
    cm_svc = confusion_matrix(y_test,y_pred_svc)
    print("-----------------------------------")
    print(cm_svc)
    plt.figure()
    plot_confusion_matrix(cm_svc)
    acc_svc_linear = accuracy_score(y_test,y_pred_svc)
    print("Accuracy SVN" + str(acc_svc_linear))
    f1_score_svn = metrics.f1_score(y_test, y_pred_svc, average='macro')
    print ("F1-score  SVN: %f" % f1_score_svn)
    precision_svn = precision_score(y_test, y_pred_svc, pos_label=3, average='macro')
    
    print("Precision  SVN " + str(precision_svn))
    recall_svn = recall_score(y_test, y_pred_svc, pos_label=3, average='macro')
    
    print("Recall  SVN " + str(recall_svn))

    print("-----------------------------------")
 #----------------------------------

def oldClass():
    
    #GridClassifier(x,y)
    
    print("prcp")
    data = new_dataTraining[['tobs']].as_matrix()
    type_label = np.where(new_dataTraining['crime']== +1,+1,-1)
    print("crime")
    print(type_label)
    x = np.array(data)
    y = np.array(type_label)
    y = np.nan_to_num(y) 
    x = np.nan_to_num(x) 
    #GridClassifier(x,y)
    
    
    
    print("snow")
    data = new_dataTraining[['tobs']].as_matrix()
    type_label = np.where(new_dataTraining['crime']== +1,+1,-1)
    print("crime")
    print(type_label)
    x = np.array(data)
    y = np.array(type_label)
    y = np.nan_to_num(y) 
    x = np.nan_to_num(x) 
    #GridClassifier(x,y)
    
"""    
x = np.array(new_dataTraining.iloc[:,:-1].values)
y = np.array(new_dataTraining.iloc[:,0].values)
print("new_dataTraining.iloc[:,:-1]")
print(new_dataTraining.iloc[:,:-1])
print("new_dataTraining.iloc[:,5]")
print(new_dataTraining.iloc[:,6])
y = np.nan_to_num(y) 
x = np.nan_to_num(x) """



print("tobs")
data = new_dataTraining[['t_high']].as_matrix()
type_label = np.where(new_dataTraining['crime']== -1,+1,-1)
print("crime")
print(type_label)
x = np.array(data)
y = np.array(type_label)
#x = np.array(new_dataTraining.iloc[:,1:-1].values)
#y = np.array(new_dataTraining.iloc[:,6].values)
#print("yyyvv")
#print(new_dataTraining.iloc[:,1:-1])
#print("xx")
#print(new_dataTraining.iloc[:,0])
y = np.nan_to_num(y) 
x = np.nan_to_num(x) 
print("here")
plt.matshow(new_dataTraining.corr())
plt.colorbar()
plt.show()
#correlationPair(x,y)

#x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.30, stratify=y)
sss = StratifiedShuffleSplit(n_splits=3, test_size=0.3, random_state=0)
x_train= [] 
x_test= []
y_train= []
y_test = []
for train_index, test_index in sss.split(x, y):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]

"----------------------------------PLOT ROC ----------------------------------" 
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

roc(y_test, y_predict_logistic)
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
roc(y_test, y_pred_svc_linear)
"----------------------------------PERCEPTRON ----------------------------------"
clf_perceptron = Perceptron(n_iter=2, shuffle=False)
clf_perceptron.fit(x_train, y_train)
y_pred_perceptron =  clf_perceptron.predict(x_test)
cm_perceptron = confusion_matrix(y_test,y_pred_perceptron)
print(cm_perceptron)
acc_perceptron = accuracy_score(y_test,y_pred_perceptron)
print("Accuracy Perceptron" + str(acc_logistic))
f1_score_perceptron = skl.metrics.f1_score(y_test, y_pred_perceptron, average='macro')
print ("F1-score Perceptron: %f" % f1_score_perceptron)
precision_perceptron = precision_score(y_test, y_pred_perceptron, pos_label=3, average='macro')

print("Precision Perceptron " + str(precision_perceptron))

recall_perceptron = recall_score(y_test, y_pred_perceptron, pos_label=3, average='macro')

print("Recall Perceptron " + str(recall_perceptron))

roc(y_test, y_pred_perceptron)

"""----------------------------------LINEAR REGRESSION ----------------------------------"""
regression = linear_model.LinearRegression()
regression.fit(x_train, y_train)
y_pred_regression = regression.predict(x_test)
score = regression.score(x_test, y_test)

"""
y2=  np.array(np.sign(y_pred_regression))
yTrain2 = np.array(np.sign(y_train))
error = np.sum((y_pred_regression-y_train)**2)
error_sum=np.sum(error)
error_sq = math.sqrt(error_sum)
print ("Residual Error for Linear Regression" + np.sign(error_sq))

print("Score for Linear Regresssion " + str(score))
"""

print('Coefficients for Linear Regression: \n', regression.coef_)

plt.figure()
plt.plot(regression.coef_, color='navy', linestyle='--')
plt.title('Coefficients for Linear Regression')
plt.show()



regression_ridge = Ridge(alpha=1.0, fit_intercept=False)
regression_ridge.fit(x_train, y_train) 
print('Coefficients for Ridge Regression: \n', regression_ridge.coef_)


plt.figure()
plt.plot(regression_ridge.coef_, color='navy', linestyle='--')
plt.title('Coefficients for Ridge Regression')
plt.show()

lasso = linear_model.Lasso(alpha=1.0)
lasso.fit(x_train, y_train)
linear_model.Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000,
   normalize=False, positive=False, precompute=False, random_state=None,
   selection='cyclic', tol=0.0001, warm_start=False)
print('Coefficients for Lasso Regression: \n', lasso.coef_)



plt.figure()
plt.plot(lasso.coef_, color='navy', linestyle='--')
plt.title('Coefficients for Lasso Regression')
plt.show()
#----------------------------------    
    
    
    
    
    
    
    
    

