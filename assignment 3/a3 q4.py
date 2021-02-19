#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


a = [[1/1, 1/2, 1/3, 1/4, 1/5],
     [1/2, 1/3, 1/4, 1/5, 1/6],
     [1/3, 1/4, 1/5, 1/6, 1/7],
     [1/4, 1/5, 1/6, 1/7, 1/8],
     [1/5, 1/6, 1/7, 1/8, 1/9]] 
b = [[1/1+1/2+1/3+1/4+1/5],
     [1/2+1/3+1/4+1/5+1/6],
     [1/3+1/4+1/5+1/6+1/7],
     [1/4+1/5+1/6+1/7+1/8],
     [1/5+1/6+1/7+1/8+1/9]] 


# In[3]:


a


# In[4]:


b


# In[5]:


a[0][1]


# In[6]:


def f1(x2,x3,x4,x5):
    x1 = ((1/1+1/2+1/3+1/4+1/5)-(((1/2)*x2)+((1/3)*x3)+((1/4)*x4)+((1/5)*x5)))/(1)
    return x1


# In[7]:


def f2(x1,x3,x4,x5):
    x2 = ((1/2+1/3+1/4+1/5+1/6)-(((1/2)*x1)+((1/4)*x3)+((1/5)*x4)+((1/6)*x5)))/(1/3)
    return x2


# In[8]:


def f3(x1,x2,x4,x5):
    x3 = ((1/3+1/4+1/5+1/6+1/7)-(((1/3)*x1)+((1/4)*x2)+((1/6)*x4)+((1/7)*x5)))/(1/5)
    return x3


# In[9]:


def f4(x1,x2,x3,x5):
    x4 = ((1/4+1/5+1/6+1/7+1/8)-(((1/4)*x1)+((1/5)*x2)+((1/6)*x3)+((1/8)*x5)))/(1/7)
    return x4


# In[10]:


def f5(x1,x2,x3,x4):
    x5 = ((1/5+1/6+1/7+1/8+1/9)-(((1/5)*x1)+((1/6)*x2)+((1/7)*x3)+((1/8)*x4)))/(1/9)
    return x5


# In[32]:





# In[11]:


#setting solytion to 0
x1=0
x2=0
x3=0
x4=0
x5=0
#list for storing values
x1l=[]
x2l=[]
x3l=[]
x4l=[]
x5l=[]


# In[12]:


#gauss seidal
for i in range(50000):
    count=0
#     print("i=",i)
    
    x1l.append(x1)
    x2l.append(x2)
    x3l.append(x3)
    x4l.append(x4)
    x5l.append(x5)
#     print("added to list")
       
    x1=f1(x2,x3,x4,x5)
#     print(x1)
    x2=f2(x1,x3,x4,x5)
#     print(x2)
    x3=f3(x1,x2,x4,x5)
#     print(x3)
    x4=f4(x1,x2,x3,x5)
#     print(x4)
    x5=f5(x1,x2,x3,x4)
#     print(x5)
#     print("executed expressions")   


# In[13]:


df = pd.DataFrame(list(zip(x1l, x2l, x3l, x4l, x5l)), 
               columns =['x1', 'x2', 'x3', 'x4','x5']) 


# In[14]:


df.tail(5)


# In[16]:


print(df.iloc[5000]) #for checking any particular iteration


# In[ ]:





# In[104]:


x1=0
x2=0
x3=0
x4=0
x5=0

x1l=[]
x2l=[]
x3l=[]
x4l=[]
x5l=[]


# In[17]:


# f1(x2,x3,x4,x5)


# In[18]:


# f2(x1,x3,x4,x5)


# In[19]:


# f3(x1,x2,x4,x5)


# In[20]:


# f4(x1,x2,x3,x5)


# In[21]:


# f5(x1,x2,x3,x4)


# In[22]:


#gauss jacobi
import math
for i in range(5000):
    count=0
#     print("\n\n")
#     print("i=",i)
       
#     print("x1t",x1t)
#     print("x2t",x2t)
#     print("x3t",x3t)
#     print("x4t",x4t)
#     print("x5t",x5t)
    x1t=f1(x2,x3,x4,x5)
    x2t=f2(x1,x3,x4,x5)
    x3t=f3(x1,x2,x4,x5)
    x4t=f4(x1,x2,x3,x5)
    x5t=f5(x1,x2,x3,x4)
    
    if abs(x1t-x1)<10**-5:
        print("reached solution")
        break
#     print("executed expressions")
    
#     print("x1",x1)
#     print("x2",x2)
#     print("x3",x3)
#     print("x4",x4)
#     print("x5",x5)
#     print("current values")
    x1=x1t
    x2=x2t
    x3=x3t
    x4=x4t
    x5=x5t
    
#     print("x1",x1)
#     print("x2",x2)
#     print("x3",x3)
#     print("x4",x4)
#     print("x5",x5)
#     print("temp val assigned")
    
    x1l.append(x1)
    x2l.append(x2)
    x3l.append(x3)
    x4l.append(x4)
    x5l.append(x5)
#     print("added to list")

    if abs(x1)==math.inf:
        print("non converging")
        break
    


# In[23]:


df2 = pd.DataFrame(list(zip(x1l, x2l, x3l, x4l, x5l)), 
               columns =['x1', 'x2', 'x3', 'x4','x5']) 


# In[24]:


df2


# In[ ]:




