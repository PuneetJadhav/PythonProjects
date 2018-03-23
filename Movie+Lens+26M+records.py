

import pandas as pd
from pandas import Series,DataFrame
import warnings
warnings.filterwarnings('ignore')

import os 
os.chdir("C:\\College\\Hadoop\\ml-latest (1)\\ml-latest")
os.getcwd()

ratings=pd.read_csv('ratings.csv',usecols=[0,1,2])

ratings.head()

## no of records loaded is as follows
len(ratings)

ratings.tail()## Data is perfect
ratings.columns

len(ratings.columns)

## check the data and change columns name
ratings.columns=["UserID","MovieID","Ratings"]

ratings[ratings['UserID'].isna()]

ratings[ratings['MovieID'].isna()]

ratings[ratings['Ratings'].isna()]


movies=pd.read_csv('movies.csv')

len(movies)

movies.head()
movies.tail()

movies.columns=["MovieID","Title","Genre"]

movie_ratings_join=movies.merge(ratings,how='inner',on='MovieID')

movie_ratings_join['MovieID']=movie_ratings_join['MovieID'].astype('object')
movie_ratings_join['UserID']=movie_ratings_join['UserID'].astype('object')

movie_ratings_join.info()

movie_ratings_join['MovieCount']=1

movie_ratings_join.groupby(['MovieID','Title','Genre']).agg({'Ratings':'mean','MovieCount':'count'}).
sort_values('Ratings',ascending=False)

movie_ratings_join.groupby(['MovieID','Title','Genre']).agg({'Ratings':'mean','MovieCount':'count'}).sort_values('MovieCount',ascending=False)

movie_ratings_join.groupby(['MovieID','Title','Genre']).agg({'Ratings':'mean','MovieCount':'count'}).sort_values(['Ratings','MovieCount'],ascending=False)

