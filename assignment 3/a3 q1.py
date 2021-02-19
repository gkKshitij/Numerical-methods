#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys


# ### First half of question that is to generate B

# In[2]:


A = np.array([[1.0,2.0,1.0],
             [2.0,3.0,3.0],
             [3.0,-1.0,2.0]])
A


# In[3]:


x=np.array([ 2., -1.,  3.])
x


# In[4]:


np.dot(A, x) #expected B


# In[ ]:





# ### Remaining part to derive x from Ax=B

# In[5]:


# Reading number of unknowns
n = 3 #int(input('number of unknowns: '))


# In[6]:


ab = np.zeros((n,n+1))
#taking input for A|B
print('Enter "A|B" matrix:')
for _ in range(n):
    for __ in range(n+1):
        ab[_][__] = float(input(f'ab{_+1}{__+1}='))


# In[7]:


ab = np.array([[1.0,2.0,1.0,3.0],
             [2.0,3.0,3.0,10.0],
             [3.0,-1.0,2.0,13.0]])


# In[8]:


ab


# In[ ]:





# In[9]:


x = np.zeros(n) #solution matrix


# In[10]:


#gauss elimination
def ge():
    for i in range(n):
        if ab[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(i+1, n):
            ratio = ab[j][i]/ab[i][i]
            for k in range(n+1):
                ab[j][k] = ab[j][k] - ratio * ab[i][k]
    return ab


# In[11]:


#back substitution
def bs():
    x[n-1] = ab[n-1][n]/ab[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = ab[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - ab[i][j]*x[j]
        x[i] = x[i]/ab[i][i]
    return x


# In[12]:


ge()


# In[13]:


bs()


# In[14]:


# Printing solution martix "x"
print('\nValues of unknown are as follows: ')
for i in range(n):
    print(f'x{i} = {x[i]}')


# In[ ]:




