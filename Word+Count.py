
# coding: utf-8

# In[9]:


import re
import os
import pandas as pd
from pandas import Series
import numpy as np
from numpy.random import randn
import warnings
warnings.filterwarnings('ignore')
os.chdir("C:\\College\\Hadoop\\SparkScala")


# In[10]:


book=open('book.txt')


# In[14]:


wordlist=[]
wordslist2=list()
for words in book:
    wordlist=re.findall('\\w+',words.strip())
    for word in wordlist:
        wordslist2.append(word)
word=Series(wordslist2)


# In[44]:


li=list(range(0,len(word)))
worddict=pd.DataFrame(word,columns=['Words'])
worddict['WordCount']=1
worddict


# In[45]:


worddict=worddict.groupby('Words').agg({'WordCount':'count'}).sort_values('WordCount',ascending=False)



# In[47]:


## to get top 5 words from the worddict or top 10
worddict[:10]

