#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path


# In[2]:


from textblob import TextBlob


# In[3]:


blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())


# In[4]:


from nltk.corpus import stopwords


# In[5]:


import nltk


# In[6]:


nltk.download('stopwords')


# In[7]:


stop_words = stopwords.words('english')


# In[8]:


items = blob.word_counts.items()
items


# In[9]:


items = [item for item in items if item[0] not in stop_words]
items


# In[10]:


from operator import itemgetter


# In[11]:


sorted_items = sorted(items, key = itemgetter(1), reverse = True)
sorted_items


# In[12]:


top20 = sorted_items[1:21]
top20


# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame(top20, columns = ['word','count'])


# In[15]:


df


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
axes = df.plot.bar(x='word', y='count', legend = False)

import matplotlib.pyplot as plt

plt.gcf().tight_layout()


# In[17]:


conda install  -c conda-forge wordcloud


# In[18]:


from pathlib import Path


# In[19]:


text = Path('RomeoAndJuliet.txt').read_text()


# In[20]:


import imageio


# In[21]:


mask_image = imageio.imread('MicrosoftTeams-image.png')


# In[22]:


from wordcloud import WordCloud


# In[23]:


WordCloud = WordCloud(width = 1000, height = 1000, 
                     colormap = 'prism',mask = mask_image, 
                     background_color = 'white')
WordCloud


# In[24]:


WordCloud = WordCloud.generate(text)
WordCloud


# In[25]:


WordCloud = WordCloud.to_file('RomeoAndJulietHeart.png')
WordCloud


# In[28]:


get_ipython().run_line_magic('matplot', 'inline')


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


plt.imshow(WordCloud)


# In[ ]:


pip install textstatistic


# In[ ]:





# In[ ]:




