
# coding: utf-8

# In[33]:


import seaborn as sns
sns.set_style('dark',{'axes.facecolor':'gray'})
get_ipython().magic('matplotlib inline')
tips=sns.load_dataset('tips')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(8,8)
plt.rcParams["patch.force_edgecolor"] = True
import numpy as np
tips.head()


# In[34]:


## Bar Plot is mostly used for categorical data
## x =categorical data, y=numerical plot
## estimator can be variance ,std deviation,mean etc
sns.barplot(data=tips,x='sex',y='total_bill',estimator=np.std)


# In[35]:


sns.countplot(x='sex',data=tips)
### Count no of males and females


# In[36]:


sns.boxplot(data=tips,x='day',y='total_bill',hue='sex')
##sns.boxplot(data=tips,x='day',y='tip',hue='sex')


# In[37]:


## Violin plot 
sns.violinplot(data=tips,x='total_bill',y='day',hue='sex',split=True)


# In[38]:


### Striplot for categorical plot
sns.stripplot(data=tips,x='day',y='total_bill',jitter=True,hue='sex')


# In[43]:


## swarmplot and violin plot together
sns.swarmplot(data=tips,x='day',y='total_bill',color='Red',hue='sex')

