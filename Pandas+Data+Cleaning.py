
# coding: utf-8

# In[1]:


import os
import warnings
import numpy as np
import pandas as pd


# In[3]:


os.chdir("C:\\College\\Python\\Pandas")
os.getcwd()


# In[4]:


warnings.filterwarnings('ignore')


# In[5]:


from numpy.random import randn


# In[6]:


data=pd.read_csv('Future-500.csv')


# In[7]:


## see top 5 rows
data.head()


# In[9]:


## see bottom rows
data.tail()


# In[10]:


## check no of rows
len(data)
### It has 500 rows


# In[11]:


## check no of columns
len(data.columns)
## There are 11 columns


# In[13]:


## columns datatypes described below
data.info()
## ID should be object
## Inception should be object
## Revenue should be float
## Expenses should be float
## Growth should be float


# In[15]:


## Convert ID and inception to object type
data['ID']=data['ID'].astype('object')
data['Inception']=data['Inception'].astype('object')


# In[40]:


### Clean the columns
### Convert columns to string or object type
data['Revenue']=data['Revenue'].astype('str')
data['Expenses']=data['Expenses'].astype('str')
data['Growth']=data['Growth'].astype('str')


# In[41]:


data.info()


# In[42]:


## String conversion and replace part
## Convert datatype of Revenue to float
data['Revenue']=data['Revenue'].str.replace('$','')
data['Revenue']=data['Revenue'].str.replace(',','')
data["Revenue"]=data["Revenue"].astype('str').astype('float')


# In[55]:


## Check first 5 rows of data of revenue 
## When we select a column a series is returened
data['Revenue'].head()


# In[44]:


## String conversion and replace part
## Convert datatype of Expenses to float
data['Expenses']=data['Expenses'].str.replace("Dollars","")
data["Expenses"]=data["Expenses"].str.replace(",","")
data["Expenses"]=data["Expenses"].astype("str").astype("float")


# In[45]:


## check first 5 rows
data["Expenses"].head()


# In[48]:


data["Growth"]
## String conversion and replace part
## Convert datatype of Growth to float
data["Growth"]=data["Growth"].str.replace("%","")
data["Growth"]=data["Growth"].astype("str").astype("float")


# In[50]:


data["Growth"].head()


# In[56]:


## checking 1st column null values
data.columns


# In[57]:


data[data["ID"].isna()]

### no null values for ID column


# In[58]:


data[data["Name"].isna()]
## no null values for name columns


# In[59]:


data[data["Industry"].isna()]


# In[69]:


data.drop(data[data["Industry"].isna()].index,inplace=True)
## Use drop function to drop all the values where Industry is NaN


# In[70]:


data[data["Industry"].isna()]


# In[71]:


len(data)


# In[74]:


data[data['Inception'].isna()]


# In[86]:


data.loc[data['Inception'].isna(),'Inception']=2006


# In[87]:


data[data['Inception'].isna()]


# In[88]:


data[data['Employees'].isna()]


# In[107]:


data[data.Industry=="Retail"]['Employees'].median()


# In[126]:


data.loc[(data['Employees'].isna()) & (data['Industry']=="Retail"),"Employees"]


# In[127]:


data.loc[(data['Employees'].isna()) & (data['Industry']=="Retail"),"Employees"]=data[data.Industry=="Retail"]['Employees'].median()


# In[128]:


data[data['Employees'].isna()]


# In[132]:


data[data.Industry=="Financial Services"]["Employees"].median()


# In[135]:


data.loc[(data["Employees"].isna()) & (data["Industry"]=="Financial Services"),"Employees"]


# In[136]:


data.loc[(data["Employees"].isna()) & (data["Industry"]=="Financial Services"),"Employees"]=data[data.Industry=="Financial Services"]["Employees"].median()


# In[137]:


data[data['Employees'].isna()]


# In[138]:


data[data['State'].isna()]


# In[142]:


data.loc[(data['State'].isna()) & (data['City']=="New York"),"State"]="New York"


# In[143]:


data[data["State"].isna()]


# In[146]:


data.loc[(data['State'].isna()) & (data['City']=='San Francisco'),"State"]="California"


# In[147]:


data[data['State'].isna()]


# In[148]:


data[data['City'].isna()]


# In[149]:


data[data['Revenue'].isna()]


# In[150]:


data[data.Industry=="Construction"]["Expenses"].median()


# In[152]:


data.loc[(data['Revenue'].isna()) & (data['Industry']=="Construction"),"Revenue"]


# In[153]:


data.loc[(data['Revenue'].isna()) & (data['Industry']=="Construction"),"Revenue"]=data[data.Industry=="Construction"]["Expenses"].median()


# In[154]:


data[data['Revenue'].isna()]


# In[155]:


data[data['Expenses'].isna()]


# In[158]:


data.loc[(data['Expenses'].isna()) & (data['Industry']=="IT Services"),"Expenses"]


# In[161]:


data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Revenue"]


# In[164]:


data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Profit"]


# In[165]:


data.loc[(data['Expenses'].isna()) & (data['Industry']=="IT Services"),"Expenses"]=data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Revenue"]-data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Profit"]


# In[166]:


data[data["Expenses"].isna()]


# In[170]:


data[data["Industry"]=="Construction"]["Expenses"].median()


# In[173]:


data.loc[(data["Expenses"].isna()) & (data["Industry"]=="Construction"),"Expenses"]


# In[174]:


data.loc[(data["Expenses"].isna()) & (data["Industry"]=="Construction"),"Expenses"]=data[data["Industry"]=="Construction"]["Expenses"].median()


# In[176]:


data[data["Profit"].isna()]


# In[179]:


data[data["Industry"]=="Construction"]["Profit"].median()


# In[181]:


data.loc[(data["Profit"].isna()) & (data["Industry"]=="Construction"),"Profit"]


# In[182]:


data.loc[(data["Profit"].isna()) & (data["Industry"]=="Construction"),"Profit"]=data[data["Industry"]=="Construction"]["Profit"].median()


# In[183]:


data[data["Profit"].isna()]


# In[184]:


data[data["Growth"].isna()]


# In[186]:


data[data["Industry"]=="Construction"]["Growth"].median()


# In[188]:


data.loc[(data["Growth"].isna()) & (data["Industry"]=="Construction"),"Growth"]


# In[189]:


data.loc[(data["Growth"].isna()) & (data["Industry"]=="Construction"),"Growth"]=data[data["Industry"]=="Construction"]["Growth"].median()

