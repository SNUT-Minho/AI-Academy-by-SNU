import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.decomposition import PCA
import time
#########################
#Load MNIST training data
train = pd.read_csv("train.csv")

#Pre-process MNIST data and split it into train, test data sets
features = train.columns[1:]
X = train[features]
y = train['label']
X_train, X_test, y_train, y_test = model_selection.train_test_split(X/255.,y,test_size=0.2,random_state=0) ## select scaling /255 make 0 to 1

"""
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2,random_state=0) ## no scaling /255 make 0 to 1
######################################

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2,random_state=0) ## standardscaler scaling
St = StandardScaler()
St.fit(X_train)
X_train = St.transform(X_train)    #standardscaler
######################################
"""


######################
#PCA decomposition training data
pca = PCA(n_components = 40) # 10, 20, 40 ,80
pca.fit(X_train)
aa = pca.explained_variance_ratio_
print np.sum(aa) # check explained variance ratio

    
#####################
#make svm classifier and fit
clf_svm = svm.SVC(kernel='rbf')  # choose kernel among "linear" "rbf" "sigmoid" "poly" 
st = time.time()
clf_svm.fit(pca.transform(X_train),y_train)
#clf_svm.fit(X_train,y_train) # not use PCA
ed = time.time()
print "training time",ed-st
st = time.time()
y_pred_svm= clf_svm.predict(pca.transform(X_test))
#y_pred_svm= clf_svm.predict(X_test) # not use PCA
#y_pred_svm= clf_svm.predict(pca.transform(St.transform(X_test))) # standardsclaer with PCA
ed = time.time()
print "test time",ed-st

#Measure accuracy of the prediction
acc_svm = accuracy_score(y_test, y_pred_svm)
print "SVM accuracy: ",acc_svm


