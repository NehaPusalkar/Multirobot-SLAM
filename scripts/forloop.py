#!/usr/bin/env python3
import numpy as np
I = [[1,2,3],[4,5,6],[7,8,9]]
M=np.matrix(I)
S=np.shape(M)
r=S[0]
c=S[1]
print(r,c)
for i in range (0,5):
   print (i)
print(I[r-1,0:2])
