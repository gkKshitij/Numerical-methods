#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Tri Diagonal Matrix Algorithm(Thomas algorithm)

# In[2]:


#driver code / question
A = np.array([[-2,1,0,0,0,0,0,0,0],
              [1,-2,1,0,0,0,0,0,0],
              [0,1,-2,1,0,0,0,0,0],
              [0,0,1,-2,1,0,0,0,0],
              [0,0,0,1,-2,1,0,0,0],
              [0,0,0,0,1,-2,1,0,0],
              [0,0,0,0,0,1,-2,1,0],
              [0,0,0,0,0,0,1,-2,1],
              [0,0,0,0,0,0,0,1,-2]],dtype=float)   


# In[3]:


alen=9#alen = len(A)
c=[]
d=[]
e=[]
for d1 in range(alen-1):
    c.append(1)
for d2 in range(alen):
    d.append(-2)
for d3 in range(alen-1):
    e.append(1)


# In[4]:


B = np.array([-1,0,0,0,0,0,0,0,-1]) 


# In[5]:


def thomasalgo(a, b, c, d):

    nf = len(d) # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d)) # copy arrays
    for it in range(1, nf):
        mc = ac[it-1]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1] 
        dc[it] = dc[it] - mc*dc[it-1]

    xc = bc
    xc[-1] = dc[-1]/bc[-1]

    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    return xc


# In[6]:


c


# In[7]:


d


# In[8]:


e


# In[9]:


B


# In[10]:


thomasalgo(c, d, e, B)


# ### comparing answers only for reference

# In[11]:


np.linalg.solve(A, B)


# In[ ]:




