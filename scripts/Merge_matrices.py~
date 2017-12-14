#!/usr/bin/env python3

import numpy as np
from scipy.linalg import block_diag

############################################### Merge_matrices #################################################################
  
#I1 = [[1,4,8],[7,6,9],[3,5,2]]
#I2 = [[1,7],[80,50],[60,9],[3,4]]

I1 = [[1,0,8],[0,6,2],[3,0,7]]
I2 = [[1,0],[2,0],[0,9],[0,4]]

#I1=[[-2,-1,0,0],[-4,0,-1,2]]
#I2=[[-2,-1,0],[0,-3,-2]]
print("Enter matrix1 elements") 
#I1 = input()                        # take matrix1 input
print(np.matrix(I1))                     
s1=np.shape(I1)                      # dimensions of matrix1
print(s1)                   
r1=s1[0];                            # get number of rows of matrix1
c1=s1[1];                            # get number of columns of matrix1

print("Enter matrix2 elements") 
#I2 = input()                        # take matrix2 input 
print(np.matrix(I2))           
s2=np.shape(I2)                      # dimensions of matrix2 
print(s2)  
r2=s2[0];                            # get number of rows of matrix2                 
c2=s2[1];                            # get number of columns of matrix2


I =block_diag(I1,I2)
r=r1+r2
c=c1+c2
print(I)

delj=[]
deli=[]

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
   print "i1=",i1
   for j1 in range(0,c1):
      print "j1=",j1
      for i2 in range(r1,r1+r2):
         print "i2=",i2
         for j2 in range(c1,c1+c2):
            print "j2=",j2 
            if (I[i1,j1]==I[i2,j2] and vertex_tag(I1,I[i1][0:c1])==vertex_tag(I2,I[i2][c1:c1+c2])): 
                print(I[i1,j1])
                if (np.sign(I[i1,j1])!=np.sign(I[i2,j2])):
                   I[i1,j1]=I[i2,j2]=(-1)*(np.absolute(I[i1,j1])) 
                if(np.count_nonzero(I[r1:r1+r2,j2])==2):                                       #non-zero element count(I[V1+1 : V1+V2, j2]) = 2 )
                   print "j1 is appended",j1
                   c1=c1-1 
                   #if c1<1:
                      #break
                   delj=np.append(delj,j1)
                   print "delj=",delj 
                   print "c1=",c1
                   
                elif(np.count_nonzero(I[0:r1,j1])==2):                                            #(non-zero element count(I[1 : V1, j1]) = 2 )
                   print "j2 is appended",j2
                   c2=c2-1
                   #if c2<1:
                      #break
                   delj=np.append(delj,j2) 
                   print "delj",delj
                   print "c2=",c2
                else:
                   print "no inference hence j1 appended",j1
                   c1=c1-1
                   #if c1<1:
                      #break
                   delj=np.append(delj,j1)   
                   print "delj",delj
                   print "c1 in final=",c1 

                if (np.count_nonzero(I[r1:r1+r2,j1])<2):                                        #if (non-zero element count(I[V1 + 1 : V1 + V2, j1] < 2) then
                   I[r1:r1+r2,j1]=I[r1:r1+r2,j1]+I[r1:r1+r2,j2]                                 #I[V1 + 1 : V1 + V2, j1] = I[V1 + 1 : V1 + V2, j1] + I[V1 + 1 : V1 + V2, j2])
                   print "changing in first loop" ,I[r1:r1+r2,j1]                   
                if (np.count_nonzero(I[0:r1,j2])<2):                                            #if (non-zero element count(I[1 : V1, j2] < 2) then
                   I[0:r1,j2]=I[0:r1,j2]+I[0:r1,j1]                                             #I[1 : V1, j2] = I[1 : V1, j2] + I[1 : V1, j1].)
                   print "changing in second loop" ,I[0:r1,j2]
                deli=np.append(deli,i1)
                print "deli=",deli

print "delj final =",delj
print "deli final =",deli
I_copy = I
print(I)
for i in range (0,len(deli)):
   if ((i!=len(deli)-1) and deli[i+1]!=deli[i]):
      I = np.delete(I,deli[i],axis=0)
      print(I)
   elif (i==len(deli)-1 and np.array_equal(I,I_copy)==True):
      I = np.delete(I,deli[i],axis=0)
      print(I)
  
 
I_copy_row=I
for j in range (0,len(delj)):
   if ((j!=len(delj)-1) and delj[j+1]!=delj[j]):
      I = np.delete(I,delj[j],axis=1)
      print(I)
   elif (j==len(delj)-1 and np.array_equal(I,I_copy_row)==True):
      I = np.delete(I,delj[j],axis=1)
      print(I)
print(I)


################################################################ Order_matrix #############################################################################








#if __name__ == '__main__':
 #   main()

            
