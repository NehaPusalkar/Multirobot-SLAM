#!/usr/bin/env python3
import numpy as np

s=np.shape(I)
r=s[0]
c=s[1]


I1=I[:,0:c1]
I2=I[:,c1:c1+c2]

print "I1 = "
print I1
print "I2 = "
print I2
count_out=0

def completed(M)
    for i in range(np.shape(M)[0]):
       if (np.count_nonzero(M[i,0:np.shape(M)[1]])==2):
         return M[i,0:np.shape(M)[1]]
       

def out(M)
    M = np.delete(M,completed(M),axis = 1)
    for i in range(np.shape(M)[0]):
       for j in range(np.shape(M)[1]):
          if (M[i,j]<0)
            return M[0:np.shape(M)[0],j]


def unexplored(M)
   M = np.delete(M,completed(M),axis = 1)
   M = np.delete(M,out(M),axis = 1)
   return M
    
I_ordered = np.column_stack(completed(I1),completed(I2),out(I1),out(I2),unexplored(I1),unexplored(I2))

EC = np.shape(completed(I1)[1]) + np.shape(completed(I2)[1])

