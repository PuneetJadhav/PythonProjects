
# coding: utf-8

# In[1]:


### Get all the necessary packages for python ####################
import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')


# In[2]:


### Get Url web page data into python
url_data=requests.get("https://en.wikipedia.org/wiki/List_of_international_cricket_centuries_by_Sachin_Tendulkar")
content=url_data.content


# In[3]:


soup=BeautifulSoup(content)


# In[4]:


div_data=soup.find('div',{'id':'mw-content-text','class':'mw-content-ltr'})
table_data_all=div_data.find_all('table')


# In[5]:


len(table_data_all)
### So we found out 5 tables ######################


# In[6]:


## table_data[1] is our data
table_data=table_data_all[1]


# In[7]:


### find the headers
sachin_century_header=[]
table_header=table_data.find_all('th')
sachin_century_header.clear()
    


# In[8]:


for header in table_header[:10]:
    sachin_century_header.append(header.get_text())


# In[9]:


sachin_century_header


# In[10]:


row_marker=0
sachin_century_tests=pd.DataFrame()
for tr in table_data.find_all('tr'):
    column_marker=0
    row_marker=row_marker+1
    for td in tr.find_all('td'):
        sachin_century_tests.loc[row_marker,column_marker]=td.get_text()
        column_marker=column_marker+1


# In[11]:


sachin_century_tests.head()
### Score is not present as its part of th hyperlink ###################


# In[12]:


### Get the scores ###################
th_class=table_data.findAll('th')
data=[]
for th in th_class:
    data.append(th.get_text())


# In[13]:


centuries=[]
for element in data[10:]:
    index=element.find("!")
    centuries.append(element[index+1:])
    


# In[14]:


for i in list(range(0,len(centuries))):
    centuries[i]=centuries[i].strip()


# In[17]:


## Got all the scores from th header #################
centuries


# In[42]:


sachin_century_tests.drop('Score',axis=1,inplace=True)


# In[65]:


sachin_century_tests
### Get the data from various columns
### Got all the countries
## Convert it into series
'''

Out[9]:
['No.',
 'Score',
 'Against',
 'Pos.',
 'Inn.',
 'Test',
 'Venue',
 'H/A',
 'Date',
 'Result']



'''

countries=sachin_century_tests[1].values
for i in list(range(0,len(countries))):
    countries[i]=countries[i].replace('\xa0','')
from pandas import Series
countries=Series(countries)


# In[66]:


## Got all the scores
scores=sachin_century_tests['9'].values
for i in list(range(0,len(scores))):
    scores[i]=scores[i].replace('\xa0','')
scores=Series(scores)    


# In[67]:


### Got all the positions
Pos=sachin_century_tests[2].values
for i in list(range(0,len(Pos))):
    Pos[i]=Pos[i].replace('\xa0','')
Pos=Series(Pos)  


# In[68]:


## Got all the innings in which he scored
Inn=sachin_century_tests[3].values
for i in list(range(0,len(Inn))):
    Inn[i]=Inn[i].replace('\xa0','')
Inn=Series(Inn) 


# In[69]:


## Got all the test
Test=sachin_century_tests[4].values
for i in list(range(0,len(Test))):
    Test[i]=Test[i].replace('\xa0','')
Test=Series(Test) 


# In[70]:


## Got all the venues
Venue=sachin_century_tests[5].values
for i in list(range(0,len(Venue))):
    Venue[i]=Venue[i].replace('\xa0','')
Venue=Series(Venue) 


# In[73]:


## Home or Away Centuries
HorA=sachin_century_tests[6].values
for i in list(range(0,len(HorA))):
    HorA[i]=HorA[i].replace('\xa0','')
HorA=Series(HorA) 


# In[74]:


##Date 
Date=sachin_century_tests[7].values
for i in list(range(0,len(Date))):
    Date[i]=Date[i].replace('\xa0','')
Date=Series(Date) 


# In[76]:


## Results
Result=sachin_century_tests[8].values
for i in list(range(0,len(Result))):
    Result[i]=Result[i].replace('\xa0','')
Result=Series(Result) 


# In[79]:


sachin_test_centuries=pd.concat([countries,scores,Pos,Inn,Test,Venue,HorA,Date,Result],axis=1)


# In[81]:


sachin_test_centuries.columns=["Country","Score","Position","Innings","Test","Venue","H/A","Date","Result"]


# In[82]:


sachin_test_centuries

