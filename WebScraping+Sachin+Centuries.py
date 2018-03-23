

### Get all the necessary packages for python ####################
import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

### Get Url web page data into python
url_data=requests.get("https://en.wikipedia.org/wiki/List_of_international_cricket_centuries_by_Sachin_Tendulkar")
content=url_data.content

soup=BeautifulSoup(content)


div_data=soup.find('div',{'id':'mw-content-text','class':'mw-content-ltr'})
table_data_all=div_data.find_all('table')

len(table_data_all)
### So we found out 5 tables ######################

## table_data[1] is our data
table_data=table_data_all[1]

### find the headers
sachin_century_header=[]
table_header=table_data.find_all('th')
sachin_century_header.clear()

for header in table_header[:10]:
    sachin_century_header.append(header.get_text())

sachin_century_header

row_marker=0
sachin_century_tests=pd.DataFrame()
for tr in table_data.find_all('tr'):
    column_marker=0
    row_marker=row_marker+1
    for td in tr.find_all('td'):
        sachin_century_tests.loc[row_marker,column_marker]=td.get_text()
        column_marker=column_marker+1

sachin_century_tests.head()
### Score is not present as its part of th hyperlink ###################

### Get the scores ###################
th_class=table_data.findAll('th')
data=[]
for th in th_class:
    data.append(th.get_text())

centuries=[]
for element in data[10:]:
    index=element.find("!")
    centuries.append(element[index+1:])

for i in list(range(0,len(centuries))):
    centuries[i]=centuries[i].strip()

## Got all the scores from th header #################
centuries

sachin_century_tests.drop('Score',axis=1,inplace=True)

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

## Got all the scores
scores=sachin_century_tests['9'].values
for i in list(range(0,len(scores))):
    scores[i]=scores[i].replace('\xa0','')
scores=Series(scores)    

### Got all the positions
Pos=sachin_century_tests[2].values
for i in list(range(0,len(Pos))):
    Pos[i]=Pos[i].replace('\xa0','')
Pos=Series(Pos)  

## Got all the innings in which he scored
Inn=sachin_century_tests[3].values
for i in list(range(0,len(Inn))):
    Inn[i]=Inn[i].replace('\xa0','')
Inn=Series(Inn) 

## Got all the test
Test=sachin_century_tests[4].values
for i in list(range(0,len(Test))):
    Test[i]=Test[i].replace('\xa0','')
Test=Series(Test) 

## Got all the venues
Venue=sachin_century_tests[5].values
for i in list(range(0,len(Venue))):
    Venue[i]=Venue[i].replace('\xa0','')
Venue=Series(Venue) 

## Home or Away Centuries
HorA=sachin_century_tests[6].values
for i in list(range(0,len(HorA))):
    HorA[i]=HorA[i].replace('\xa0','')
HorA=Series(HorA) 

##Date 
Date=sachin_century_tests[7].values
for i in list(range(0,len(Date))):
    Date[i]=Date[i].replace('\xa0','')
Date=Series(Date) 

## Results
Result=sachin_century_tests[8].values
for i in list(range(0,len(Result))):
    Result[i]=Result[i].replace('\xa0','')
Result=Series(Result) 

sachin_test_centuries=pd.concat([countries,scores,Pos,Inn,Test,Venue,HorA,Date,Result],axis=1)

sachin_test_centuries.columns=["Country","Score","Position","Innings","Test","Venue","H/A","Date","Result"]
print(sachin_test_centuries)

