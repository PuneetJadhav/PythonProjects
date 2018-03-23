
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('dark',{'axes.facecolor':'Black'})
get_ipython().magic('matplotlib inline')

plt.rcParams['figure.figsize']=(8,6)
plt.rcParams['patch.force_edgecolor']=True

import os
import warnings
os.chdir("C:\\Users\\PuneetPC\\Downloads")
warnings.filterwarnings('ignore')
from numpy.random import randn

movies=pd.read_csv('Movie-Ratings (1).csv')
movies.columns=['Film','Genre','CriticsRatings','AudienceRatings','Budget','ReleaseYear']
movies['ReleaseYear']=movies['ReleaseYear'].astype('object')


tips=sns.load_dataset('tips')
tips.head()

### Distribution plot
### One variable plot
sns.distplot(tips.total_bill,bins=30,color="Red")

### Joint Plot
### 2 variable plots
## type 1
sns.jointplot(data=tips,x=tips.total_bill,y=tips.tip,size=10,kind='hex')

## type 2 (default scatter plot)
sns.jointplot(data=tips,x=tips.total_bill,y=tips.tip,size=10)

## type 3 reg
sns.jointplot(data=tips,x=tips.total_bill,y=tips.tip,size=10,kind='reg')

## type 4
sns.jointplot(data=tips,x=tips.total_bill,y=tips.tip,size=10,kind='kde')
plt.show()

### pair plot
## compare each pair with each other
## eg total_bill vs total_bill, total_bill vs tips,total_bill vs size
sns.pairplot(tips,size=5,hue='sex')

