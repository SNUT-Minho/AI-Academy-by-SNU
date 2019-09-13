from scipy import ndimage
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
import sys

im = ndimage.imread(sys.argv[1], mode='L')
#plt.imshow(im, cmap=matplotlib.cm.Greys_r)
#plt.show()

newim=np.invert(im, dtype='uint8')
#plt.imshow(newim, cmap=matplotlib.cm.Greys_r)
#plt.show()

newim = misc.imresize(newim,(28,28))
outf=sys.argv[1].split('png')[0]+"csv"
newim.ravel().tofile(outf,sep=',')
