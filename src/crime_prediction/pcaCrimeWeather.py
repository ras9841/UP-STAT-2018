
"""
Using pca for data exploration.
"""
#Import libraries.
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np
import matplotlib.pyplot as plt

#reading the file
df = pd.read_csv("../../data/crime_prediction/weather-crime.csv")

cities = df[['category']]
data = df.drop(['x','y','date','category'], axis=1)
column_names = data.columns
data = data.fillna(0)
#data, results = convert_categorical_to_number(new_dataTraining)

matrix = (data).as_matrix()
print(matrix)
matrix_scale = scale(matrix, axis=0, with_mean=True, with_std=True, copy=True)


pca =PCA(None, copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None)
pca.fit(matrix_scale)
matrix_norm = pca.transform(matrix_scale)
variance_ratio = pca.explained_variance_ratio_
print(variance_ratio) 
print("*******")
singular_value = pca.singular_values_
print(singular_value)
print("*******")
explained_variance = pca.explained_variance_
print(explained_variance) 
print("*******")
mean = pca.mean_
print(mean) 
print("*******")
n_components = pca.n_components_
print(n_components) 
print("*******")
noise_variance = pca.noise_variance_
print(noise_variance) 
print("*******")
loading_vectors =pca.components_.T * np.sqrt(pca.explained_variance_)
print(loading_vectors)
print("*******cumsum")
print pca.explained_variance_ratio_.cumsum()

#Plot explained variance ratio as a function of number of principal components. 
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');

#What are minimum number of principal components needed to explain at least 80% of the variance in the data 
#answer: 5

#List the loading vectors for the first 3 principal components and interpret them.
#
print("PCA COMPONENTS")
PCA_1 = loading_vectors[:1] 
print(PCA_1)

PCA_2 = loading_vectors[1:2] 
print(PCA_2)

PCA_3 = loading_vectors[2:3] 
print(PCA_3)


pca = PCA(n_components=3).fit(matrix_scale)
transformedData = pca.transform(matrix_scale)   
transformedData = pd.DataFrame(transformedData, columns = ['PCA 1', 'PCA 2', 'PCA 3'])

def biplotPC(data, reduced_data, pca,labelPCAA, labelPCAB):
    figure, axes = plt.subplots(figsize = (14,8))
    x=reduced_data.loc[:, labelPCAA]
    y=reduced_data.loc[:, labelPCAB]
    axes.scatter(x, y, facecolors='blue', edgecolors='blue', s=80, alpha=0.5)
    feature_vectors_values = pca.components_.T
    arrow_size, text_position = 7.0, 9.0,
    for index, value in enumerate(feature_vectors_values):
        axes.text(value[0] * text_position, value[1] * text_position, column_names[index], color='red', ha='center', va='center', fontsize=14)
        axes.arrow(0, 0, arrow_size * value[0], arrow_size * value[1], head_width=0.15, head_length=0.15, linewidth=1.5, color='red')

            
    axes.set_xlabel(labelPCAA, fontsize=16)
    axes.set_ylabel(labelPCAB, fontsize=16)
    axes.set_title("%s - %s" % (labelPCAA,labelPCAB), fontsize=16);

biplotPC(matrix_scale, transformedData, pca, 'PCA 1', 'PCA 2')
biplotPC(matrix_scale, transformedData, pca, 'PCA 1', 'PCA 3')
biplotPC(matrix_scale, transformedData, pca, 'PCA 2', 'PCA 3')





