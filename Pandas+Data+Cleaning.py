
import os
import warnings
import numpy as np
import pandas as pd

os.chdir("C:\\College\\Python\\Pandas")
os.getcwd()

warnings.filterwarnings('ignore')
from numpy.random import randn

data=pd.read_csv('Future-500.csv')

## see top 5 rows
data.head()
## see bottom rows
data.tail()

## check no of rows
len(data)
### It has 500 rows

## check no of columns
len(data.columns)
## There are 11 columns

## columns datatypes described below
data.info()
## ID should be object
## Inception should be object
## Revenue should be float
## Expenses should be float
## Growth should be float

## Convert ID and inception to object type
data['ID']=data['ID'].astype('object')
data['Inception']=data['Inception'].astype('object')

### Clean the columns
### Convert columns to string or object type
data['Revenue']=data['Revenue'].astype('str')
data['Expenses']=data['Expenses'].astype('str')
data['Growth']=data['Growth'].astype('str')

data.info()

## String conversion and replace part
## Convert datatype of Revenue to float
data['Revenue']=data['Revenue'].str.replace('$','')
data['Revenue']=data['Revenue'].str.replace(',','')
data["Revenue"]=data["Revenue"].astype('str').astype('float')

## Check first 5 rows of data of revenue 
## When we select a column a series is returened
data['Revenue'].head()


## String conversion and replace part
## Convert datatype of Expenses to float
data['Expenses']=data['Expenses'].str.replace("Dollars","")
data["Expenses"]=data["Expenses"].str.replace(",","")
data["Expenses"]=data["Expenses"].astype("str").astype("float")

## check first 5 rows
data["Expenses"].head()

data["Growth"]
## String conversion and replace part
## Convert datatype of Growth to float
data["Growth"]=data["Growth"].str.replace("%","")
data["Growth"]=data["Growth"].astype("str").astype("float")


data["Growth"].head()

## checking 1st column null values
data.columns

data[data["ID"].isna()]

### no null values for ID column

data[data["Name"].isna()]
## no null values for name columns


data[data["Industry"].isna()]

data.drop(data[data["Industry"].isna()].index,inplace=True)
## Use drop function to drop all the values where Industry is NaN

data[data["Industry"].isna()]

len(data)

data[data['Inception'].isna()]

data.loc[data['Inception'].isna(),'Inception']=2006


data[data['Inception'].isna()]


data[data['Employees'].isna()]

data[data.Industry=="Retail"]['Employees'].median()


data.loc[(data['Employees'].isna()) & (data['Industry']=="Retail"),"Employees"]

data.loc[(data['Employees'].isna()) & (data['Industry']=="Retail"),"Employees"]=data[data.Industry=="Retail"]['Employees'].median()

data[data['Employees'].isna()]

data[data.Industry=="Financial Services"]["Employees"].median()

data.loc[(data["Employees"].isna()) & (data["Industry"]=="Financial Services"),"Employees"]

data.loc[(data["Employees"].isna()) & (data["Industry"]=="Financial Services"),"Employees"]=data[data.Industry=="Financial Services"]["Employees"].median()

data[data['Employees'].isna()]

data[data['State'].isna()]

data.loc[(data['State'].isna()) & (data['City']=="New York"),"State"]="New York"

data[data["State"].isna()]

data.loc[(data['State'].isna()) & (data['City']=='San Francisco'),"State"]="California"

data[data['State'].isna()]

data[data['City'].isna()]

data[data['Revenue'].isna()]

data[data.Industry=="Construction"]["Expenses"].median()

data.loc[(data['Revenue'].isna()) & (data['Industry']=="Construction"),"Revenue"]

data.loc[(data['Revenue'].isna()) & (data['Industry']=="Construction"),"Revenue"]=data[data.Industry=="Construction"]["Expenses"].median()

data[data['Revenue'].isna()]

data[data['Expenses'].isna()]

data.loc[(data['Expenses'].isna()) & (data['Industry']=="IT Services"),"Expenses"]

data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Revenue"]

data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Profit"]

data.loc[(data['Expenses'].isna()) & (data['Industry']=="IT Services"),"Expenses"]=data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Revenue"]-data.loc[(data["Expenses"].isna()) & (data["Industry"]=="IT Services"),"Profit"]

data[data["Expenses"].isna()]

data[data["Industry"]=="Construction"]["Expenses"].median()

data.loc[(data["Expenses"].isna()) & (data["Industry"]=="Construction"),"Expenses"]

data.loc[(data["Expenses"].isna()) & (data["Industry"]=="Construction"),"Expenses"]=data[data["Industry"]=="Construction"]["Expenses"].median()

data[data["Profit"].isna()]

data[data["Industry"]=="Construction"]["Profit"].median()

data.loc[(data["Profit"].isna()) & (data["Industry"]=="Construction"),"Profit"]

data.loc[(data["Profit"].isna()) & (data["Industry"]=="Construction"),"Profit"]=data[data["Industry"]=="Construction"]["Profit"].median()

data[data["Profit"].isna()]

data[data["Growth"].isna()]

data[data["Industry"]=="Construction"]["Growth"].median()


data.loc[(data["Growth"].isna()) & (data["Industry"]=="Construction"),"Growth"]

data.loc[(data["Growth"].isna()) & (data["Industry"]=="Construction"),"Growth"]=data[data["Industry"]=="Construction"]["Growth"].median()

