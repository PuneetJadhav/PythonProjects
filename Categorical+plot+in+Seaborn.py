import seaborn as sns
sns.set_style('dark',{'axes.facecolor':'gray'})
get_ipython().magic('matplotlib inline')
tips=sns.load_dataset('tips')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(8,8)
plt.rcParams["patch.force_edgecolor"] = True
import numpy as np
tips.head()
## Bar Plot is mostly used for categorical data
## x =categorical data, y=numerical plot
## estimator can be variance ,std deviation,mean etc
sns.barplot(data=tips,x='sex',y='total_bill',estimator=np.std)
sns.countplot(x='sex',data=tips)
### Count no of males and females

sns.boxplot(data=tips,x='day',y='total_bill',hue='sex')
##sns.boxplot(data=tips,x='day',y='tip',hue='sex')

## Violin plot 
sns.violinplot(data=tips,x='total_bill',y='day',hue='sex',split=True)


### Striplot for categorical plot
sns.stripplot(data=tips,x='day',y='total_bill',jitter=True,hue='sex')

## swarmplot and violin plot together
sns.swarmplot(data=tips,x='day',y='total_bill',color='Red',hue='sex')
sns.violinplot(data=tips,x='total_bill',y='day',hue='sex',split=True)
