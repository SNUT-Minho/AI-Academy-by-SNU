import math
import graphviz
import csv
import numpy as np 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

def entropy(arr):
	classCounts = np.unique(arr, return_counts=True)[1]
	sampleNum = arr.shape[0]
	if sampleNum==0:
		return 0
	p_arr = classCounts / float(sampleNum)
	ret = -np.log(p_arr)*p_arr
	return sum(ret)

def gini(arr):
	classCounts = np.unique(arr, return_counts=True)[1]
	sampleNum = arr.shape[0]
	p_arr = classCounts / float(sampleNum)
	ret = 1. - (p_arr**2).sum()
	return ret

def giniSplit(arr1, arr2):
	sampleNum1 = float(arr1.shape[0])
	sampleNum2 = float(arr2.shape[0])
	totalSampleNum = sampleNum1 + sampleNum2
#	return entropy(arr1) * sampleNum1 / totalSampleNum + \
	#	   entropy(arr2) * sampleNum2 / totalSampleNum
	return gini(arr1) * sampleNum1 / totalSampleNum + \
		   gini(arr2) * sampleNum2 / totalSampleNum


df = pd.read_csv('winequality-red.csv', delimiter=';')
print df.head()

df.loc[df['quality']>5,'quality'] = 'good'
df.loc[df['quality']<=5,'quality'] = 'bad'

print df.head()
ind = range(len(df['quality']))
ind = np.array(ind)
ind = ind%4!=0
train = df[ind==True]
test = df[ind==False]
features = df.columns[:11]
train_x = train[features]
train_y = train['quality']
test_x = test[features]
test_y = test['quality']


minGiniSplit = np.inf
minSplitFeature = None
minSplitBoundary = None
feature = train_x


for fIdx in range(feature.shape[1]):
	featureArr = train_x[train_x.columns[fIdx]]
	uniqueSorted = np.unique(np.sort(featureArr))
	for i in range(len(uniqueSorted)-1):
		splitBoundary = (uniqueSorted[i] + uniqueSorted[i+1]) / 2.
		split1 = train_y[featureArr <= splitBoundary]
		split2 = train_y[featureArr > splitBoundary]
		giniSplitValue = giniSplit(split1, split2)

		if giniSplitValue < minGiniSplit:
			minGiniSplit = giniSplitValue
			minSplitFeature = fIdx
			minSplitBoundary = splitBoundary


print 'minSplitValue:     {}'.format(minGiniSplit)
print 'minSplitFeature:   {}'.format(train_x.columns[minSplitFeature])
print 'minSplitBoundary:  {}'.format(minSplitBoundary)
