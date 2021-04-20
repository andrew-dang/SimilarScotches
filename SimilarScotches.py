# -*- coding: utf-8 -*-
"""
SimilarScotches
Written by Andrew Dang


"""


import pandas as pd 
import numpy as np 
from sklearn.neighbors import NearestNeighbors

# load the dataset 
inFile = 'Path\to\scotch_data.xlsx'
df = pd.read_excel(inFile)

#remove label and index from dataset to prepare it for KNN
X = df.copy()
X.drop(['NAME', 'INDEX'], axis=1, inplace=True)

# KNN model
nbrs = NearestNeighbors(n_neighbors=109, metric = 'jaccard').fit(X)
distances, indices = nbrs.kneighbors(X)   

# replace index number with name of distiller
whiskey = df['NAME'].tolist()
index = df['INDEX'].tolist()

SimilarScotches = np.zeros(len(indices))
for i in index:
    SimilarScotches = np.where(indices == i, whiskey[i], SimilarScotches)
 
# assign each scotch to an index; this is so I can choose a reference
scotch_to_idx = { scotch:i for i, scotch in enumerate(whiskey)}

# print name of scotches for user
print(df['NAME'])

# Ask user to input name of scotch. Then print names of similar scotches and their distances
Reference = input('Select a scotch from the list above: ')
print('The further down the list, the more different that scotch is to the one you have selected')

name_of_scotch = SimilarScotches[scotch_to_idx[Reference]]
distance_from_reference = distances[scotch_to_idx[Reference]]

scotch_and_distances = pd.DataFrame({'Scotch': name_of_scotch, 'Distance': distance_from_reference})
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(scotch_and_distances)