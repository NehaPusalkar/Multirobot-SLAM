#!/usr/bin/env python3

import numpy as np
from scipy.linalg import block_diag

I1 = [[1,4,8],[7,6,9],[3,5,2]]
I2 = [[1,7],[8,5],[6,9],[3,4]]
print("Enter matrix1 elements") 
#I1 = input()                         # take matrix1 input
print(np.matrix(I1))                     
s1=np.shape(I1)                      # dimensions of matrix1
print(s1)                   
r1=s1[0];                            # get number of rows of matrix1
c1=s1[1];                            # get number of columns of matrix1

print("Enter matrix2 elements") 
#I2 = input()                         # take matrix2 input 
print(np.matrix(I2))           
s2=np.shape(I2)                      # dimensions of matrix2 
print(s2)  
r2=s2[0];                            # get number of rows of matrix2                 
c2=s2[1];                            # get number of columns of matrix2


I =block_diag(I1,I2)
r=r1+r2
c=c1+c2
print(I)

def vertex_tag(matrix,row):
 if matrix == "I1":
   for i in range(0,r1):
       val = cmp(row,I1[i:])
       if val==0:
         return i
       else:
         return -1
 elif matrix == "I2": 
   for j in range(0,r2):
      val = cmp(row,I2[i:])
      if val==0:
         return i
      else:
         return -1
      
for i1 in range(0,r1):
   for j1 in range(0,c1):
      for i2 in range(r1,r1+r2):
         for j2 in range(c1,c1+c2):
            if (I[i1,j1]==I[i2,j2] and vertex_tag(I1,I[i1:])==vertex_tag(I2,I[i2:])): 
                print(I[i1,j1])
           

             
