
# coding: utf-8

# In[7]:


import pandas as pd
from pandas import Series,DataFrame
import warnings
warnings.filterwarnings('ignore')


# In[8]:


import os 
os.chdir("C:\\College\\Hadoop\\ml-latest (1)\\ml-latest")
os.getcwd()


# In[12]:


ratings=pd.read_csv('ratings.csv',usecols=[0,1,2])


# In[13]:


ratings.head()


# In[14]:


## no of records loaded is as follows
len(ratings)


# In[15]:


ratings.tail()## Data is perfect


# In[16]:


ratings.columns


# In[17]:


len(ratings.columns)


# In[18]:


## check the data and change columns name
ratings.columns=["UserID","MovieID","Ratings"]


# In[19]:


ratings[ratings['UserID'].isna()]


# In[20]:


ratings[ratings['MovieID'].isna()]


# In[21]:


ratings[ratings['Ratings'].isna()]


# In[22]:


movies=pd.read_csv('movies.csv')


# In[23]:


len(movies)


# In[27]:


movies.head()
movies.tail()


# In[26]:


movies.columns=["MovieID","Title","Genre"]


# In[28]:


movie_ratings_join=movies.merge(ratings,how='inner',on='MovieID')


# In[31]:


movie_ratings_join['MovieID']=movie_ratings_join['MovieID'].astype('object')
movie_ratings_join['UserID']=movie_ratings_join['UserID'].astype('object')


# In[33]:


movie_ratings_join.info()


# In[43]:


movie_ratings_join['MovieCount']=1


# In[47]:


movie_ratings_join.groupby(['MovieID','Title','Genre']).agg({'Ratings':'mean','MovieCount':'count'}).
sort_values('Ratings',ascending=False)


# In[48]:


movie_ratings_join.groupby(['MovieID','Title','Genre']).agg({'Ratings':'mean','MovieCount':'count'}).sort_values('MovieCount',ascending=False)


# In[49]:


movie_ratings_join.groupby(['MovieID','Title','Genre']).agg({'Ratings':'mean','MovieCount':'count'}).sort_values(['Ratings','MovieCount'],ascending=False)

