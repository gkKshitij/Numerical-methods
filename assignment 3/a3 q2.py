#!/usr/bin/env python
# coding: utf-8

# # LU decomposition

# In[1]:


from numpy import dot
from numpy import zeros,array,product,diagonal
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
import numpy
import numpy as np


# In[2]:


#array from question 1
a = np.array([[1.0,2.0,1.0],
             [2.0,3.0,3.0],
             [3.0,-1.0,2.0]])


# In[3]:


b=np.array([ 3., 10.0,  13.0])


# In[4]:


def LUdecomp(a):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
    return a


# In[5]:


a


# In[6]:


a[0][1]


# In[7]:


a = LUdecomp(a)


# In[8]:


a


# In[9]:


rows=len(a)
cols=len(a[0])


# In[10]:


def mzm(rows: int, cols: int): #make zero matrix
    matrix = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            if i==j:
                matrix[i][j]=1
            else:
                matrix[i][j]=0
    m = numpy.array(matrix) 
    return m


# In[11]:


L=mzm(3,3)


# In[12]:


U=mzm(3,3)


# In[13]:


U


# In[14]:


def makel(a,L,U):
    dc=0 #diagonal counter
    for i in range(rows):
        dc=dc+1
        for j in range(cols):
            if j<dc-1:
                L[i][j]=a[i][j]
            else:
                U[i][j]=a[i][j]
    return a,L,U


# In[15]:


makel(a,L,U)


# In[16]:


v = np.linalg.solve(L, b)
v


# In[17]:


x = np.linalg.solve(U, v)
x

