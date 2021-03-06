#!/usr/bin/env python3

import numpy as np
from scipy.linalg import block_diag

I1 = [[1,0,8],[0,6,0],[0,0,0]]
I2 = [[1,0],[0,0],[0,9],[0,4]]
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
count1=0
count2=0


   
def main():
           

 p=np.count_nonzero(I[:,4]);
 print(p)
 print(I[r1:r1+r2,4])
 print(I[r1:r1+r2,4][0:2])


if __name__ == '__main__':
    main()
