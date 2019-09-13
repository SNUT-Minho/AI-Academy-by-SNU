import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
#################
# Load iris data form web
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target']) # read_csv with header
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values # loc: find values using labels
y = df.loc[:,['target']].values

x = StandardScaler().fit_transform(x) # data standardzation

#################
# PCA fitting and transformation
pca = PCA(n_components=2)
pca.fit(x)
fitted_data = pca.transform(x)
print (pca.explained_variance_ratio_)
    
################
# plotting
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)

targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r','g','b']
for target, color in zip(targets,colors):
    ind = y == target
    ax.scatter(fitted_data[:,0].reshape(150,1)[ind], fitted_data[:,1].reshape(150,1)[ind]
               , c = color
                , s = 50)
ax.legend(targets)
ax.grid()
plt.show()

