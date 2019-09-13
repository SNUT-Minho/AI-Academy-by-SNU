import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
##########
# generating random xor data
xx, yy = np.meshgrid(np.linspace(-3, 3, 500), # for plotting decision line
                     np.linspace(-3, 3, 500))
np.random.seed(0)
X = np.random.randn(300, 2)      # xor data
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)

##########
# SVM classifier traning
#clf = svm.SVC(kernel="linear")
clf = svm.SVC(kernel="rbf")
clf.fit(X, Y)
#########
# plot the decision function for each datapoint on the grid
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y,edgecolors='k',cmap=plt.cm.Paired) # point
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2, # decision line
                       linetypes='--')
plt.imshow(Z, interpolation='nearest',  
          extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
          origin='lower', cmap=plt.cm.PuOr_r)

plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
