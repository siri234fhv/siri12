#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# In[2]:


l1=[10,20,30,40,50,60,70]
print(l1,type(l1))


# In[3]:


a=np.array(l1)
print(a,type(a))


# In[4]:


t=(10,20,30,40,50)
print(t,type(t))


# In[6]:


a=np.array(t)
print(a,type(a))


# In[7]:


d1={10:1.2,20:34,30:76,98:20}
print(d1,type(d1))


# In[8]:


a=np.array(d1)
print(a,type(a))


# In[20]:


t=(10,20,30,40,50,60)
a=np.array(t)


# In[21]:


a


# In[22]:


a.ndim


# In[23]:


a.shape


# In[24]:


a.dtype


# In[26]:


b=a.reshape(2,3)


# In[27]:


b


# In[30]:


b=a.reshape(3,2)
b


# In[31]:


t1=((10,20),(30,40))
print(t1,type(t1))


# In[32]:


a=np.array(t1)


# In[33]:


a


# In[34]:


a.ndim


# In[35]:


a.shape


# In[36]:


t1=((10,20,30),(30,40,70),(67,27,48),(67,38,29))
print(t1,type(t1))


# In[39]:


a=np.array(t1)
a


# In[38]:


a.ndim


# In[40]:


a.shape


# In[41]:


t1=((10,20,30),(30,40,70)),((67,27,48),(67,38,29))
print(t1,type(t1))


# In[42]:


a=np.array(t1)
a


# In[43]:


a.ndim


# In[45]:


a.shape


# In[48]:


b=a.reshape(4,3)
b


# In[49]:


c=a.reshape(3,4)
c


# In[52]:


d=a.reshape(3,2,2)
d


# In[53]:


d[0]


# In[54]:


d[1]


# In[55]:


d[2]


# # arange

# In[57]:


a=np.arange(10)
a


# In[64]:


a.ndim


# In[65]:


a=np.arange(10,23,2)
a


# In[66]:


a=np.arange(10,22,2)
a


# In[63]:


a=np.arange(1,10,3)
a


# In[67]:


a.ndim


# In[68]:


a.shape


# In[70]:


b=a.reshape(3,2)
b


# In[71]:


b.ndim


# In[72]:


l1=[ [[10,20],[30,40]], [[15,25],[35,45]] ]
a=np.array(l1)
a


# In[73]:


l1=[ [[10,20],[30,40]], [[15,25],[35,45]] ]
a=np.arange(l1)
a


# # $Zeros()

# In[74]:


import numpy as np


# In[76]:


a=np.zeros(10)
a


# In[77]:


a=np.zeros(12,dtype=int)
a


# In[78]:


a.reshape(3,4)


# In[79]:


a.reshape(4,3)


# In[80]:


a.reshape(6,2)


# In[81]:


a.reshape(2,6)


# In[83]:


a.reshape(2,3,2)


# In[84]:


a.reshape(2,2,3)


# In[85]:


import numpy as np


# In[86]:


a=np.zeros((3,3),dtype=int)
a


# In[89]:


a=np.zeros((2,3))
a


# In[90]:


a=np.zeros((2,3),dtype=int)
a


# In[91]:


a=np.zeros((2,3,2),dtype=int)
a


# $Ones()

# In[92]:


import numpy as np


# In[93]:


a=np.ones(10)
a


# In[11]:


a=np.ones(10,dtype=int)
a


# In[96]:


a=np.ones((4,3),dtype=int)
a


# In[97]:


a.shape=(3,2,2)
a


# In[13]:


a=np.ones((4,3,3),dtype=int)
a


# In[18]:


ar2=np.zeros((5,7,6),dtype=int)+8 #shape(cell,rows,column)
ar2


# In[17]:


ar2.ndim


# $Full

# In[ ]:





# In[101]:


a=np.full(3,1)
a


# In[103]:


a=np.full(3,9)
a


# In[104]:


a=np.full(6,8)
a


# In[105]:


a=np.full(6,9)
a


# In[106]:


a.reshape(2,3)


# In[107]:


a=np.full((2,3),6)
a


# In[108]:


a.reshape(3,2)


# In[109]:


a=np.full((3,3,3),7)
a


# $Identity

# In[111]:


a=np.identity(3,dtype=int)
a


# In[112]:


a=np.identity(5,dtype=int)
a


# In[113]:


a=np.identity(6,dtype=int)
a


# $Numpy.hstack()

# In[114]:


a = np.array([1, 2, 3]) 
b=np.array([3,5,6])
np.hstack((a,b))


# In[115]:


a = np.array([[1, 2], [3, 4]]) 
b = np.array([[4, 5, 6], [7, 8, 9]])
np.hstack((a,b))


# In[9]:


a = np.array([[1, 2], [3, 4]]) 
b = np.array([[4, 5, 6], [7, 8, 9]])
np.hstack((a,b))


# $numpy.vstack()

# In[118]:


a = np.array([1, 2, 3]) 
b=np.array([3,5,6])
np.vstack((a,b))


# In[122]:


c =np.array([[1, 2], [3,4]])
d = np.array([[4, 5], [5,6]])
np.vstack((c,d))


# In[129]:


a = np.array([[1, 2], [3,4]])
b = np.array([[4, 5], [5,6]])
np.vstack((a,b))


# In[133]:


a=np.full((3,3,3),"HYD")
print(a,type(a))



# In[132]:


a.ndim


# In[134]:


a.shape


# In[135]:


a=np.full((3,3),"HYD")
print(a,type(a))


# In[136]:


a=np.full((3,3),fill_value="HYD")
print(a,type(a))


# In[137]:


a=np.full((3,3),fill_value=8)
print(a,type(a))


# In[138]:


a=np.full((2,3,3),fill_value=8)
print(a,type(a))


# In[140]:


a=np.full(6,2)
a


# In[141]:


a.ndim


# In[143]:


a.shape


# In[145]:


a=random.randint(10,20)
a


# In[21]:


np.random.randint(10)


# In[23]:


np.random.randint(10,50)


# In[24]:


np.random.randint(10,50,(3,3,2))


# In[27]:


np.random.rand(2,3,5)


# In[ ]:


#Converting 1-D Array to 2-D Array


# In[31]:


ar4=np.arange(12)
ar4


# In[32]:


ar4.ndim


# In[34]:


ar4.reshape(4,3)


# In[35]:


ar4.reshape(6,2)


# In[36]:


ar4.min()


# In[37]:


ar4.max()


# In[38]:


ar4.mean()


# ar4.sum()

# In[40]:


ar4.sum()


# In[41]:


ar4.std()


# In[42]:


ar4.max(axis=0)


# In[44]:


ar4


# In[45]:


ar4.max(axis=0)


# In[48]:


ar=np.array([1,2,3,4,5,6])
ar


# In[49]:


ar.reshape((2,3))


# In[50]:


import array


# In[51]:


array.array("i",(1,2,3,5))


# In[58]:


ar2=np.full((2,3),6)
ar2


# In[53]:


import random


# In[62]:


#random values
np.random.seed(21)
ar3=np.random.randint(0,10,(2,3))
ar3


# In[66]:


ar3.reshape(3,2)


# In[67]:


ar3.max(axis=0)


# In[68]:


ar3.max(axis=1)


# In[69]:


#builtin
sum([1,2,3,4])


# In[72]:


ar3


# In[70]:


ar3.sum(axis=1)


# In[71]:


ar3.sum(axis=0)


# $Identity$

# In[1]:


import numpy as np


# In[6]:


a=np.identity(3,) #By default it will take float
a


# In[7]:


a=np.identity(3,dtype=int)
a


# In[8]:


a=np.identity(5,dtype=int)
a


# In[ ]:




