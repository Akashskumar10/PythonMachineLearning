import numpy as np
import os
x=np.arange(16).reshape(4,4)
header='c1 c2 c3 c4'
np.savetxt('7_array.txt',x,fmt="%d",header=header)
print("\nAfter loading,content of the text file:")
print(np.loadtxt('7_array.txt'))