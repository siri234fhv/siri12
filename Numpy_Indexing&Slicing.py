#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.array([10,20,30,40,50,60])
print(a,type(a))


# In[3]:


a[0]


# In[4]:


a[-2]


# In[5]:


a[-4]


# In[ ]:


#Basic Indexing 2-D Array


# In[6]:


a=np.array([10,20,30,40,50,60])
a.shape=(3,2)
print(a,type(a))


# In[7]:


a[0:1,0:1]


# In[8]:


a[1,1]


# In[9]:


a[-2,-2]


# In[10]:


a=np.array([10,20,30,40,50,60,70,80,90])
a.shape=(3,3)
print(a,type(a))


# In[ ]:


#+ve index


# In[21]:


#i want 50
a[1::,1::]


# In[22]:


a[1:2:,1:2:]


# In[14]:


a[1:2,0:1]


# In[25]:


#60
a[1,2]


# In[26]:


# -60
a[-2,-1]


# ar3

# In[28]:


a


# In[30]:


# -20
a[-3,-2]


# In[31]:


a[-1,-2]


# In[34]:


a[-2][-3]


# In[32]:


a[-2,-3]


# In[33]:


a[-2][-3]


# $n-Array$

# In[43]:


a=np.array([10,20,40,30,76,37,19,38,39,62,89,51])
a.shape=(2,3,2)
print(a,type(a))


# In[44]:


a[0,0,0]


# In[45]:


a[1,1,1]


# In[46]:


# -40 
a[-2,-2,-2]


# In[47]:


a[-1,-2,-2]


# In[48]:


a[0]


# In[49]:


a[1]


# In[56]:


a1=np.array([10,20,40,30,76,37,19,38,39,62,89,51,45,44,76,88])


# In[59]:


a1.shape=(2,2,2,2)
a1


# In[60]:


#+ve i want 38
a1[0]


# 

# In[61]:


a1[1]


# In[66]:


a1[0,0]


# In[67]:


a1[0,0,1]


# In[68]:


a1[0,0,1,1]


# In[71]:


a1[1,1,1,1]


# In[72]:


a1[1,0,1,0]


# In[73]:


a1


# In[76]:


a1[-1,-2,-1,-2]


# In[77]:


a1[-2,-2,-1,-2]


# In[78]:


a1[-2,-1,-1,-1]


# In[82]:


import random


# In[88]:


import numpy as np


# In[139]:


np.random.seed(21)
ar1=np.random.randint(1,10,(3,4,3))
ar1


# In[140]:


ar1[0:1:,2:3:,1::]


# In[141]:


ar1[1:2,2:4,1:2]


# 

# In[142]:


ar1[0::,0::2,1:2]


# In[143]:


ar1


# In[100]:


ar1[0::,2::,1::]


# In[144]:


ar1[0:2:,0::3,0:2:]


# In[145]:


ar1


# In[146]:


ar1[0:1,3::,1:2]


# In[147]:


ar1[2::,2:3,0:2]


# In[148]:


ar1[-3:-2,-1::,-2:-1:]


# In[149]:


ar1[-2:-1,-2:-1,-3:-2]


# In[ ]:





# $-Ve Slicing$

# In[150]:


ar1[-2:-1,-2:-1:,-3:-2]


# In[151]:


ar1[-3:-2,-3:-2,-2:-1]


# In[152]:


ar1[-3::,-2::,-3:-2]


# In[153]:


ar1[-3::,-4::2,-3:-1]


# In[154]:


ar2=np.transpose(ar1)
ar2


# In[155]:


ar1


# In[156]:


#asarray() is a function in various programming libraries, such as NumPy, that is used to convert an input into an array
input_data=[1,2,3,4,5]
numpy_array=np.array(input_data)


# In[157]:


numpy_array


# In[169]:


#fromarray() function is commonly associated with the Python Imaging Library (PIL) or its fork, Pillow, which is a popular library for image processing in Python. The fromarray() function is used to create an image object from a NumPy array or an array-like structure. 
from PIL import Image
import numpy as np

# Create a NumPy array representing an image
image_array = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]], dtype=np.uint8)

# Convert the NumPy array to a Pillow image using fromarray()
image = Image.fromarray(image_array)

# Display the image (for demonstration purposes)
image.show()



# In[163]:


import numpy 


# In[165]:


# dstack() function is used to stack arrays in sequence along the third axis (depth-wise). It's primarily used for working with three-dimensional arrays or volumes. This means that dstack() takes a sequence of arrays and stacks them along a new third dimension, creating a new three-dimensional array.

#numpy.dstack(tup)
#tup: A sequence of input arrays to be stacked along the third axis. These arrays must have the same shape along all axes except for the third axis.

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Stack the arrays along the third axis using dstack
result = np.dstack((array1, array2))

print("Array 1:")
print(array1)

print("Array 2:")
print(array2)

print("Result (Stacked along the third axis):")
print(result)


# In[166]:


array1 = np.array([1, 2])
array2 = np.array([5, 6])
result = np.dstack((array1, array2))


# In[167]:


result


# In[170]:


#fromiter()
import numpy as np
python_list = [1, 2, 3, 4, 5]

# Use fromiter() to create a NumPy array from the iterable
numpy_array = np.fromiter(python_list, dtype=int)

# Display the resulting NumPy array
print(numpy_array)


# In[ ]:




