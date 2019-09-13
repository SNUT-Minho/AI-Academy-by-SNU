from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
import numpy as np
import random
#Data load
iris = load_iris()
print(iris.data)
print(iris.target)
ind = range(150)
random.shuffle(ind)
iris.data = iris.data[ind]
iris.target = iris.target[ind]

iris_train_x = iris.data[:-50]
iris_test_x = iris.data[-50:]
iris_train_y = iris.target[:-50]
iris_test_y = iris.target[-50:]
#print iris_train_y
#Build Decision Tree Classifier Model
clf = tree.DecisionTreeClassifier()

#Fit Model to iris data
#clf = clf.fit(iris.data, iris.target)
clf = clf.fit(iris_train_x, iris_train_y)

#Draw decision tree
#tree.export_graphviz(clf,out_file="tree_result.dot") 
dot_data = tree.export_graphviz(clf, out_file="tree_result_color.dot",\
                        feature_names=iris.feature_names,\
                        class_names=iris.target_names,\
                        filled=True, rounded=True,\
                        special_characters=False)

#graph = graphviz.Source("test.dot")
#graph.render(iris)
predict = clf.predict(iris_test_x)
print(predict)


#Compute correct prediction rate
numOfCorrectPrediction = (predict == iris_test_y).sum()  # It should be 150
numOfDataSamples = len(iris_test_y)  # Total number of sampels. It also should be 150.

print numOfCorrectPrediction / float(numOfDataSamples)
