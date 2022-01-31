#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
Mid_1 = [70,58,85,82,70,40,85,85]
Mid_2 = [88,52,84,74,80,36,48,96]
plt.scatter(Mid_1, Mid_2) 
plt.xlabel("Midterm 1") 
plt.ylabel("Midterm 2")
plt.show()


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
Mid_1 = np.array([70,58,85,82,70,40,85,85])
Mid_2 = np.array([88,52,84,74,80,36,48,96])
plt.plot(Mid_1, Mid_2, 'o')
m, b = np.polyfit(Mid_1, Mid_2, 1)
#m = slope, b=intercept
print(m)
print(b)

plt.plot(Mid_1, (m*Mid_1 + b))
plt.xlabel('Midterm 1')
plt.ylabel('Midterm 2')
plt.show()


# In[5]:


import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt

data = np.random.randint(0,12,size=72)
bins = np.arange(13)-0.5

hist, edges = np.histogram(data, bins=bins)

y = np.arange(1,hist.max()+1)
x = np.arange(12)
X,Y = np.meshgrid(x,y)

plt.scatter(X,Y, c=Y<=hist, cmap="Greys")

plt.show() 


# In[9]:


from scipy.stats import binom
# setting the values of n and p
n = 3
p = 0.8
# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))


# In[ ]:





# In[ ]:




