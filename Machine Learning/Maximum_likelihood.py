import numpy as np
def lh(x):
	return (5*np.log(x))+(5*np.log(1-x))
a = range(5,100,5)
a = np.array(a,dtype=float)
a/=100
res = [lh(x) for x in a]
max = max(res)
max_index = np.argmax(res)
print ("Maximum Likelihood : %f" % max)
print ("Parameter : %f" % a[max_index])
