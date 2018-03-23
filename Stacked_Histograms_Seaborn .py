
import seaborn as sns
import pandas as pd
import numpy as np
import os
import warnings
os.chdir("C:\\Users\\PuneetPC\\Downloads")
warnings.filterwarnings('ignore')
from numpy.random import randn
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']= 10,12
plt.rcParams["patch.force_edgecolor"] = True
get_ipython().magic('matplotlib inline')

movies=pd.read_csv('Movie-Ratings (1).csv')
movies.head()
movies.columns=['Film','Genre','CriticsRatings','AudienceRatings','Budget','ReleaseYear']
movies['ReleaseYear']=movies['ReleaseYear'].astype('object')

sns.set_style('darkgrid')

##Stacked Histograms 
genre_array=movies.Genre.unique()

genre_array
genre_label=list()

for genre in genre_array:
    if genre=='Comedy':
        genre_label.append(genre)
        comedy_budget=movies[movies.Genre=='Comedy']['Budget']
    elif genre=='Adventure':
        genre_label.append(genre)
        adventure_budget=movies[movies.Genre=='Adventure']['Budget']
    elif genre=='Action':
        action_budget=movies[movies.Genre=='Action']['Budget']
        genre_label.append(genre)
    elif genre=='Horror':
        horror_budget=movies[movies.Genre=='Horror']['Budget']
        genre_label.append(genre)
    elif genre=='Drama':
        drama_budget=movies[movies.Genre=='Drama']['Budget']
        genre_label.append(genre)
    elif genre=='Romance':
        romance_budget=movies[movies.Genre=='Romance']['Budget']
        genre_label.append(genre)
    else:
        thriller_budget=movies[movies.Genre=='Thriller']['Budget']
        genre_label.append(genre)

### create a stacked histograms in matplotlib
combined_list=[comedy_budget,adventure_budget,action_budget,horror_budget,drama_budget,romance_budget,thriller_budget]
plt.hist(combined_list,bins=20,stacked=True,label=genre_label)
plt.rcParams['figure.figsize'] = 12,10
plt.legend()
plt.show()

